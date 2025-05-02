import pandas as pd
from config import (
    BASE_PITCHING_RATES,
    PITCHING_COMPONENTS_ADJUST_MAP,
    PITCHING_WOBA_WEIGHTS,
    HANDEDNESS_WEIGHTS,
    MINIMUM_STARTER_PITCHES,
    MINIMUM_RELIEVER_PITCHES,
    MINIMUM_STARTER_STAMINA,
    RUNS_PER_GAME_PITCHING_COEFF,
    RUNS_PER_GAME_PITCHING_CONST,
    RUNS_PER_WIN,
    RELIEVER_VS_STARTER_AVERAGE_IP
)

def calc_pitching_metrics(df: pd.DataFrame) -> pd.DataFrame:

    # establish whether a pitcher is a starter or reliever
    def identify_role(row):
        if row["pitches"] >= MINIMUM_STARTER_PITCHES and row["stamina"] >= MINIMUM_STARTER_STAMINA:
            return "sp"
        elif row["pitches"] >= MINIMUM_RELIEVER_PITCHES:
            return "rp"
        else:
            return ""

    df["sprp"] = df.apply(identify_role, axis=1)

    # Helper function to adjust rates
    def adjust_rates(row, side):
        rates = {
            "hr_vs": BASE_PITCHING_RATES["hr_vs_baserate"],
            "bb_vs": BASE_PITCHING_RATES["bb_vs_baserate"],
            "k_vs": BASE_PITCHING_RATES["k_vs_baserate"],
            "h_nothr_vs": BASE_PITCHING_RATES["h_nothr_vs_baserate"]
        }
        ratings = {
            "Control": row[f"ctrl{side}"],
            "pBABIP": row[f"pbabip{side}"],
            "HRA": row[f"hra{side}"],
            "Stuff": row[f"stuff{side}"],
            "Stamina": row["stamina"]
        }

        for category, value in ratings.items():
            table = PITCHING_COMPONENTS_ADJUST_MAP[category]
            keys = list(map(int, table.keys()))
            min_key = min(keys)
            max_key = max(keys)
            str_value = str(value)

            if category == "Stamina":
                if str_value not in table:
                    continue
                adj = table[str_value]
            else:
                if pd.isna(value) or int(value) < min_key:
                    min_adj = table[str(min_key)]
                    adj = {k: 10 * v for k, v in min_adj.items()}
                elif int(value) > max_key:
                    adj = table[str(max_key)]
                else:
                    adj = table[str_value]

            rates["hr_vs"] += adj["hr_vs_adj"]
            rates["bb_vs"] += adj["bb_vs_adj"]
            rates["k_vs"] += adj["k_vs_adj"]
            rates["h_nothr_vs"] += adj["h_nothr_vs_adj"]

        return pd.Series({
            f"hr_vs{side}": rates["hr_vs"],
            f"bb_vs{side}": rates["bb_vs"],
            f"k_vs{side}": rates["k_vs"],
            f"h_nothr_vs{side}": rates["h_nothr_vs"]
        })

    # Apply rating adjustments to base rates for RHH and LHH
    rates_r = df.apply(lambda row: adjust_rates(row, "R"), axis=1)
    rates_l = df.apply(lambda row: adjust_rates(row, "L"), axis=1)
    df = pd.concat([df, rates_r, rates_l], axis=1)

    # Only calculate pWOBA for valid pitchers
    valid_pitcher = df["sprp"].isin(["sp", "rp"])

    df["pwOBAR"] = (
        PITCHING_WOBA_WEIGHTS["hr_vs_wOBA_weight"] * df["hr_vsR"] +
        PITCHING_WOBA_WEIGHTS["bb_vs_wOBA_weight"] * df["bb_vsR"] +
        PITCHING_WOBA_WEIGHTS["h_nothr_vs_wOBA_weight"] * df["h_nothr_vsR"]
    ).where(valid_pitcher)

    df["pwOBAL"] = (
        PITCHING_WOBA_WEIGHTS["hr_vs_wOBA_weight"] * df["hr_vsL"] +
        PITCHING_WOBA_WEIGHTS["bb_vs_wOBA_weight"] * df["bb_vsL"] +
        PITCHING_WOBA_WEIGHTS["h_nothr_vs_wOBA_weight"] * df["h_nothr_vsL"]
    ).where(valid_pitcher)

    df["pwOBA"] = (
        df["pwOBAR"] * HANDEDNESS_WEIGHTS["R"] +
        df["pwOBAL"] * HANDEDNESS_WEIGHTS["L"]
    ).where(valid_pitcher)

    # convert pitcher wOBA to pitcher WAR (relievers earn less WAR than starters due to fewer IP)
    df["war_pitching"] = -((df["pwOBA"] * RUNS_PER_GAME_PITCHING_COEFF) - RUNS_PER_GAME_PITCHING_CONST) / RUNS_PER_WIN
    df["war_pitching"] = df["war_pitching"].round(1)
    df["is_sp"] = (df["sprp"] == "sp").astype(int)
    df["is_rp"] = (df["sprp"] == "rp").astype(int)
    df["war_pitching"] = df["war_pitching"] * (df["is_sp"] + (df["is_rp"] * RELIEVER_VS_STARTER_AVERAGE_IP))
    df.loc[~df["sprp"].isin(["sp", "rp"]), "war_pitching"] = pd.NA
    df["sp_war"] = df["war_pitching"] * df["is_sp"]
    df["rp_war"] = df["war_pitching"] * df["is_rp"]
    df.loc[df["war_pitching"].isna(), ["sp_war", "rp_war"]] = pd.NA

    return df


# Calculate pitching metrics based on potential ratings (no handedness)
def calc_potential_pitching_metrics(df: pd.DataFrame) -> pd.DataFrame:

    # establish whether a pitcher is a starter or reliever based on potential
    def identify_role(row):
        if row["pitchesP"] >= MINIMUM_STARTER_PITCHES and row["stamina"] >= MINIMUM_STARTER_STAMINA:
            return "sp"
        elif row["pitchesP"] >= MINIMUM_RELIEVER_PITCHES:
            return "rp"
        else:
            return ""

    df["sprpP"] = df.apply(identify_role, axis=1)

    # Helper function to adjust rates using potential ratings (no handedness)
    def adjust_rates(row):
        rates = {
            "hr_vs": BASE_PITCHING_RATES["hr_vs_baserate"],
            "bb_vs": BASE_PITCHING_RATES["bb_vs_baserate"],
            "k_vs": BASE_PITCHING_RATES["k_vs_baserate"],
            "h_nothr_vs": BASE_PITCHING_RATES["h_nothr_vs_baserate"]
        }
        ratings = {
            "Control": row["ctrlP"],
            "pBABIP": row["pbabipP"],
            "HRA": row["hraP"],
            "Stuff": row["stuffP"],
            "Stamina": row["stamina"]
        }

        for category, value in ratings.items():
            table = PITCHING_COMPONENTS_ADJUST_MAP[category]
            keys = list(map(int, table.keys()))
            min_key = min(keys)
            max_key = max(keys)
            str_value = str(value)

            if category == "Stamina":
                if str_value not in table:
                    continue
                adj = table[str_value]
            else:
                if pd.isna(value) or int(value) < min_key:
                    min_adj = table[str(min_key)]
                    adj = {k: 10 * v for k, v in min_adj.items()}
                elif int(value) > max_key:
                    adj = table[str(max_key)]
                else:
                    adj = table[str_value]

            rates["hr_vs"] += adj["hr_vs_adj"]
            rates["bb_vs"] += adj["bb_vs_adj"]
            rates["k_vs"] += adj["k_vs_adj"]
            rates["h_nothr_vs"] += adj["h_nothr_vs_adj"]

        return pd.Series(rates)

    # Apply potential rating adjustments
    rates = df.apply(adjust_rates, axis=1)
    df = pd.concat([df, rates], axis=1)

    # Only calculate pWOBA for valid potential pitchers
    valid_pitcher = df["sprpP"].isin(["sp", "rp"])

    df["pwOBAP"] = (
        PITCHING_WOBA_WEIGHTS["hr_vs_wOBA_weight"] * df["hr_vs"] +
        PITCHING_WOBA_WEIGHTS["bb_vs_wOBA_weight"] * df["bb_vs"] +
        PITCHING_WOBA_WEIGHTS["h_nothr_vs_wOBA_weight"] * df["h_nothr_vs"]
    ).where(valid_pitcher)

    df["war_pitchingP"] = -((df["pwOBAP"] * RUNS_PER_GAME_PITCHING_COEFF) - RUNS_PER_GAME_PITCHING_CONST) / RUNS_PER_WIN
    df["war_pitchingP"] = df["war_pitchingP"].round(1)

    df["is_spP"] = (df["sprpP"] == "sp").astype(int)
    df["is_rpP"] = (df["sprpP"] == "rp").astype(int)
    df["war_pitchingP"] = df["war_pitchingP"] * (df["is_spP"] + (df["is_rpP"] * RELIEVER_VS_STARTER_AVERAGE_IP))
    df.loc[~df["sprpP"].isin(["sp", "rp"]), "war_pitchingP"] = pd.NA
    df["sp_warP"] = df["war_pitchingP"] * df["is_spP"]
    df["rp_warP"] = df["war_pitchingP"] * df["is_rpP"]

    return df