def calc_war(df):
    """
    Adds WAR per position by combining fielding and hitting WAR.
    """
    df["C"] = df["C_def"] + df["war_hitting"]
    df["CF"] = df["CF_def"] + df["war_hitting"]
    df["RF"] = df["RF_def"] + df["war_hitting"]
    df["LF"] = df["LF_def"] + df["war_hitting"]
    df["SS"] = df["SS_def"] + df["war_hitting"]
    df["2B"] = df["2B_def"] + df["war_hitting"]
    df["3B"] = df["3B_def"] + df["war_hitting"]
    df["1B"] = df["1B_def"] + df["war_hitting"]
    df["DH"] = df["DH_hitting"] 
    # identify the position with highest WAR for each player
    war_columns = ["C", "CF", "RF", "LF", "SS", "2B", "3B", "1B", "DH"]
    df["best"] = df[war_columns].max(axis=1)
    df["pos"] = df[war_columns].idxmax(axis=1)

    df["CP"] = df["C_def"] + df["war_hittingP"]
    df["CFP"] = df["CF_def"] + df["war_hittingP"]
    df["RFP"] = df["RF_def"] + df["war_hittingP"]
    df["LFP"] = df["LF_def"] + df["war_hittingP"]
    df["SSP"] = df["SS_def"] + df["war_hittingP"]
    df["2BP"] = df["2B_def"] + df["war_hittingP"]
    df["3BP"] = df["3B_def"] + df["war_hittingP"]
    df["1BP"] = df["1B_def"] + df["war_hittingP"]
    df["DHP"] = df["DH_hittingP"]

    # identify the position with highest potential WAR for each player
    war_potential_columns = ["CP", "CFP", "RFP", "LFP", "SSP", "2BP", "3BP", "1BP", "DHP"]
    df["bestP"] = df[war_potential_columns].max(axis=1)
    df["posP"] = df[war_potential_columns].idxmax(axis=1)
    return df