from pathlib import Path

# =============
# Project Paths
# =============

filepath = Path('/Users/archie/Application Support/Out of the Park Developments/OOTP Baseball 26/saved_games/cubs_ootp26.lg/import_export/csv')
export_filepath = Path('/Users/archie/Desktop/Stuff/squirrel_plays/Pistachio/outputs')
pistachio_filepath = Path('/Users/archie/Desktop/Stuff/squirrel_plays/Pistachio')

# ========================
# User & Team Identifiers
# ========================

ID = 3332 # this is your scout's coach_id taken from coaches.csv
team_managed = 'CHC'  

# ======================
# Club Lookup Map
# ======================
# This maps team/org ID numbers to team abbreviations (e.g. 6 → "CHC")
# You can edit this dictionary if OOTP changes club IDs or you want to rename them

club_lookup = {
    0:  "Free",
    1:  "AZ",
    2:  "ATL",
    3:  "BAL",
    4:  "BOS",
    5:  "CWS",
    6:  "CHC",
    7:  "CIN",
    8:  "CLE",
    9:  "COL",
    10: "DET",
    11: "MIA",
    12: "HOU",
    13: "KC",
    14: "LAA",
    15: "LAD",
    16: "MIL",
    17: "MIN",
    18: "NYY",
    19: "NYM",
    20: "OAK",
    21: "PHI",
    22: "PIT",
    23: "SD",
    24: "SEA",
    25: "SF",
    26: "STL",
    27: "TB",
    28: "TEX",
    29: "TOR",
    30: "WSH"
}

# ============================
# Fielding rating thresholds to be viewed as 'can field' at that position
# ============================

POSITION_THRESHOLDS = {
    "C":  [("Cfram", 65), ("Cabil", 55), ("Carm", 35)],
    "CF": [("OFrange", 70), ("OFarm", 50)],
    "RF": [("OFrange", 50), ("OFarm", 40)],
    "LF": [("OFrange", 50), ("OFarm", 30)],
    "SS": [("IFrange", 65), ("IFerror", 50), ("IFarm", 40)],
    "2B": [("IFrange", 55), ("IFarm", 60), ("turnDP", 50)],
    "3B": [("IFrange", 50), ("IFerror", 35), ("IFarm", 60)],
}

# ============================
# Pitcher rating thresholds used to determine if a pitcher is a starter or reliever
# ============================

PITCH_MINIMUM_RATING = 45 # used to establish 'how many pitches' a pitcher has
MINIMUM_STARTER_STAMINA = 40
MINIMUM_STARTER_PITCHES = 3
MINIMUM_RELIEVER_PITCHES = 2

# =================
# Metric Constants
# =================

RUNS_PER_WIN = 10
REPLACEMENT_LEVEL_WOBA = 0.3 # no positional adjustment
REPLACEMENT_LEVEL_PITCHER_WOBA = 0.36

# Regression of wOBA vs runs/162 games for pitchers; this is the slope and intercept of the regression line
RUNS_PER_GAME_PITCHING_COEFF = 646.6961042
RUNS_PER_GAME_PITCHING_CONST = 206.0579547

# same regression for hitters
RUNS_PER_GAME_HITTING_COEFF = 554.7865342
RUNS_PER_GAME_HITTING_CONST = 178.9071431

RELIEVER_VS_STARTER_AVERAGE_IP = 0.3333333 # relievers assumed to pitch one-third of the innings of a starter, on average
DH_PENALTY = 0.023 # penalty to expected wOBA for being a DH (i.e. not playing defense)
HANDEDNESS_WEIGHTS = {
    "R": 0.7,
    "L": 0.3
}

# ============================
# Columns Used from Each CSV
# ============================

# —— players.csv ——
PLAYERS_COLUMNS = [
    "player_id",
    "first_name",
    "last_name",
    "age",
    "team_id",
    "organization_id",
    "retired"
]

# —— players_career_pitching_stats.csv ——
PITCHING_STATS_COLUMNS = [
    "player_id",
    "ip",
    "level_id",
    "split_id",
    "year"
]

# —— players_career_batting_stats.csv ——
HITTING_STATS_COLUMNS = [
    "player_id",
    "year",
    "level_id",
    "split_id",
    "pa"
]

# —— players_scouted_ratings.csv ——
SCOUTED_RATINGS_COLUMNS = [
    "player_id",
    "scouting_coach_id",
    "pitching_ratings_vsr_control",
    "pitching_ratings_vsr_pbabip",
    "pitching_ratings_vsr_hra",
    "pitching_ratings_vsr_stuff",
    "pitching_ratings_vsl_control",
    "pitching_ratings_vsl_pbabip",
    "pitching_ratings_vsl_hra",
    "pitching_ratings_vsl_stuff",
    "pitching_ratings_misc_stamina",
    "pitching_ratings_talent_control",
    "pitching_ratings_talent_pbabip",
    "pitching_ratings_talent_hra",
    "pitching_ratings_talent_stuff",
    "batting_ratings_vsr_power",
    "batting_ratings_vsr_eye",
    "batting_ratings_vsr_strikeouts",
    "batting_ratings_vsr_gap",
    "batting_ratings_vsr_babip",
    "batting_ratings_vsl_power",
    "batting_ratings_vsl_eye",
    "batting_ratings_vsl_strikeouts",
    "batting_ratings_vsl_gap",
    "batting_ratings_vsl_babip",
    "batting_ratings_talent_power",
    "batting_ratings_talent_eye",
    "batting_ratings_talent_strikeouts",
    "batting_ratings_talent_gap",
    "batting_ratings_talent_babip",
    "running_ratings_speed",
    "fielding_ratings_catcher_framing",
    "fielding_ratings_catcher_ability",
    "fielding_ratings_catcher_arm",
    "fielding_ratings_outfield_range",
    "fielding_ratings_outfield_arm",
    "fielding_ratings_outfield_error",
    "fielding_ratings_infield_range",
    "fielding_ratings_infield_error",
    "fielding_ratings_infield_arm",
    "fielding_ratings_turn_doubleplay"
]

PITCH_RATING_COLUMNS = [
    "pitching_ratings_pitches_fastball",
    "pitching_ratings_pitches_slider",
    "pitching_ratings_pitches_curveball",
    "pitching_ratings_pitches_screwball",
    "pitching_ratings_pitches_forkball",
    "pitching_ratings_pitches_changeup",
    "pitching_ratings_pitches_sinker",
    "pitching_ratings_pitches_splitter",
    "pitching_ratings_pitches_knuckleball",
    "pitching_ratings_pitches_cutter",
    "pitching_ratings_pitches_circlechange",
    "pitching_ratings_pitches_knucklecurve"
]

POTENTIAL_PITCH_RATING_COLUMNS = [
    'pitching_ratings_pitches_talent_fastball',
    'pitching_ratings_pitches_talent_slider',
    'pitching_ratings_pitches_talent_curveball',
    'pitching_ratings_pitches_talent_screwball',
    'pitching_ratings_pitches_talent_forkball',
    'pitching_ratings_pitches_talent_changeup',
    'pitching_ratings_pitches_talent_sinker',
    'pitching_ratings_pitches_talent_splitter',
    'pitching_ratings_pitches_talent_knuckleball',
    'pitching_ratings_pitches_talent_cutter',
    'pitching_ratings_pitches_talent_circlechange',
    'pitching_ratings_pitches_talent_knucklecurve'
]

# =================================
# Column Renames by CSV
# =================================

# —— players.csv ——
PLAYERS_COLUMN_RENAMES = {
    "organization_id": "org"
}

# —— players_scouted_ratings.csv ——
SCOUTED_RATINGS_RENAMES = {
    "pitching_ratings_vsr_control": "ctrlR",
    "pitching_ratings_vsr_pbabip": "pbabipR",
    "pitching_ratings_vsr_hra": "hraR",
    "pitching_ratings_vsr_stuff": "stuffR",
    "pitching_ratings_vsl_control": "ctrlL",
    "pitching_ratings_vsl_pbabip": "pbabipL",
    "pitching_ratings_vsl_hra": "hraL",
    "pitching_ratings_vsl_stuff": "stuffL",
    "pitching_ratings_talent_control": "ctrlP",
    "pitching_ratings_talent_pbabip": "pbabipP",
    "pitching_ratings_talent_hra": "hraP",
    "pitching_ratings_talent_stuff": "stuffP",
    "pitching_ratings_misc_stamina": "stamina",
    "batting_ratings_vsr_power": "powR",
    "batting_ratings_vsr_eye": "eyeR",
    "batting_ratings_vsr_strikeouts": "avkR",
    "batting_ratings_vsr_gap": "gapR",
    "batting_ratings_vsr_babip": "babipR",
    "batting_ratings_vsl_power": "powL",
    "batting_ratings_vsl_eye": "eyeL",
    "batting_ratings_vsl_strikeouts": "avkL",
    "batting_ratings_vsl_gap": "gapL",
    "batting_ratings_vsl_babip": "babipL",
    "batting_ratings_talent_power": "powP",
    "batting_ratings_talent_eye": "eyeP",
    "batting_ratings_talent_strikeouts": "avkP",
    "batting_ratings_talent_gap": "gapP",
    "batting_ratings_talent_babip": "babipP",
    "fielding_ratings_catcher_framing": "Cfram",
    "fielding_ratings_catcher_ability": "Cabil",
    "fielding_ratings_catcher_arm": "Carm",
    "fielding_ratings_outfield_range": "OFrange",
    "fielding_ratings_outfield_arm": "OFarm",
    "fielding_ratings_outfield_error": "OFerror",
    "fielding_ratings_infield_range": "IFrange",
    "fielding_ratings_infield_error": "IFerror",
    "fielding_ratings_infield_arm": "IFarm",
    "fielding_ratings_turn_doubleplay": "turnDP"
}

# ===================
# Rename Helper
# ===================

def rename_columns(df, old, new):
    if old in df.columns:
        print(f"🔁 Renaming column: {old} → {new}")
        return df.rename(columns={old: new})
    else:
        print(f"⚠️ Column {old} not found — skipping rename")
        return df

# ================================
# Columns to Blank Before Export
# ================================
COLUMNS_TO_BLANK_BEFORE_EXPORT = [
    "pwOBA",
    "pwOBAR",
    "pwOBAL",
    "sp_war",
    "rp_war"
]

# ============================
# wOBA and wRC+ weights
# ============================

# Base rates for a pitcher with all 50 ratings
BASE_PITCHING_RATES = {
    "hr_vs_baserate": 0.0326,
    "bb_vs_baserate": 0.0714,
    "k_vs_baserate": 0.2078,
    "h_nothr_vs_baserate": 0.2050
}

# Run-Value Weights for Pitching wOBA (pwOBA) calculation
PITCHING_WOBA_WEIGHTS = {
    "hr_vs_wOBA_weight": 1.95,
    "bb_vs_wOBA_weight": 0.72,
    "h_nothr_vs_wOBA_weight": 0.99
}

# Base rates for a hitter with all 50 ratings
BASE_HITTING_RATES = {
    "hr_pct_baserate": 0.0333,
    "k_pct_baserate": 0.2089,
    "bb_pct_baserate": 0.0706,
    "1b_pct_baserate": 0.1564,
    "2b_pct_baserate": 0.0450,
    "3b_pct_baserate": 0.0048
}

# Run-Value Weights for hitter wOBA calculation
BATTING_WOBA_WEIGHTS = {
    "hr_pct_wOBA_weight": 1.95,
    "bb_pct_wOBA_weight": 0.72,
    "1b_pct_wOBA_weight": 0.90,
    "2b_pct_wOBA_weight": 1.24,
    "3b_pct_wOBA_weight": 1.56
}

# league context for wRC+
LEAGUE_WOBA        = 0.320        # from all-50 hitter calibration
WOBA_SCALE         = 1.15         # from Tango book
LEAGUE_RUNS_PER_PA = 0.120        

# ===============================================
# Pitching wOBA component adjustments by rating
# ===============================================

PITCHING_COMPONENTS_ADJUST_MAP = {
    "Control": {
        "35": {"hr_vs_adj": -0.0022, "bb_vs_adj":  0.0486, "k_vs_adj": -0.0122, "h_nothr_vs_adj": -0.0132},
        "40": {"hr_vs_adj": -0.0016, "bb_vs_adj":  0.0349, "k_vs_adj": -0.0081, "h_nothr_vs_adj": -0.0092},
        "45": {"hr_vs_adj": -0.0012, "bb_vs_adj":  0.0176, "k_vs_adj": -0.0038, "h_nothr_vs_adj": -0.0047},
        "50": {"hr_vs_adj":  0.0000, "bb_vs_adj":  0.0000, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0000},
        "55": {"hr_vs_adj":  0.0006, "bb_vs_adj": -0.0083, "k_vs_adj":  0.0016, "h_nothr_vs_adj":  0.0019},
        "60": {"hr_vs_adj":  0.0004, "bb_vs_adj": -0.0135, "k_vs_adj":  0.0039, "h_nothr_vs_adj":  0.0034},
        "65": {"hr_vs_adj":  0.0005, "bb_vs_adj": -0.0173, "k_vs_adj":  0.0052, "h_nothr_vs_adj":  0.0043},
        "70": {"hr_vs_adj":  0.0005, "bb_vs_adj": -0.0222, "k_vs_adj":  0.0058, "h_nothr_vs_adj":  0.0058},
        "75": {"hr_vs_adj":  0.0010, "bb_vs_adj": -0.0264, "k_vs_adj":  0.0069, "h_nothr_vs_adj":  0.0069},
        "80": {"hr_vs_adj":  0.0018, "bb_vs_adj": -0.0315, "k_vs_adj":  0.0088, "h_nothr_vs_adj":  0.0063}
    },
    "pBABIP": {
        "35": {"hr_vs_adj":  0.0003, "bb_vs_adj": -0.0003, "k_vs_adj": -0.0009, "h_nothr_vs_adj":  0.0067},
        "40": {"hr_vs_adj": -0.0005, "bb_vs_adj": -0.0012, "k_vs_adj":  0.0012, "h_nothr_vs_adj": -0.0001},
        "45": {"hr_vs_adj": -0.0003, "bb_vs_adj": -0.0010, "k_vs_adj":  0.0002, "h_nothr_vs_adj":  0.0026},
        "50": {"hr_vs_adj":  0.0000, "bb_vs_adj":  0.0000, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0000},
        "55": {"hr_vs_adj":  0.0002, "bb_vs_adj": -0.0005, "k_vs_adj":  0.0008, "h_nothr_vs_adj": -0.0021},
        "60": {"hr_vs_adj":  0.0001, "bb_vs_adj": -0.0006, "k_vs_adj": -0.0003, "h_nothr_vs_adj": -0.0032},
        "65": {"hr_vs_adj":  0.0001, "bb_vs_adj": -0.0008, "k_vs_adj":  0.0008, "h_nothr_vs_adj": -0.0048},
        "70": {"hr_vs_adj": -0.0001, "bb_vs_adj":  0.0002, "k_vs_adj":  0.0005, "h_nothr_vs_adj": -0.0083}
    },
    "HRA": {
        "35": {"hr_vs_adj":  0.0286, "bb_vs_adj": -0.0013, "k_vs_adj":  0.0012, "h_nothr_vs_adj": -0.0094},
        "40": {"hr_vs_adj":  0.0217, "bb_vs_adj": -0.0004, "k_vs_adj":  0.0003, "h_nothr_vs_adj": -0.0073},
        "45": {"hr_vs_adj":  0.0110, "bb_vs_adj": -0.0008, "k_vs_adj":  0.0012, "h_nothr_vs_adj": -0.0030},
        "50": {"hr_vs_adj":  0.0000, "bb_vs_adj":  0.0000, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0000},
        "55": {"hr_vs_adj": -0.0040, "bb_vs_adj": -0.0007, "k_vs_adj":  0.0010, "h_nothr_vs_adj":  0.0014},
        "60": {"hr_vs_adj": -0.0071, "bb_vs_adj": -0.0004, "k_vs_adj":  0.0003, "h_nothr_vs_adj":  0.0023},
        "65": {"hr_vs_adj": -0.0096, "bb_vs_adj": -0.0006, "k_vs_adj":  0.0008, "h_nothr_vs_adj":  0.0026},
        "70": {"hr_vs_adj": -0.0112, "bb_vs_adj": -0.0005, "k_vs_adj": -0.0006, "h_nothr_vs_adj":  0.0030},
        "75": {"hr_vs_adj": -0.0141, "bb_vs_adj": -0.0002, "k_vs_adj": -0.0001, "h_nothr_vs_adj":  0.0043},
        "80": {"hr_vs_adj": -0.0170, "bb_vs_adj": -0.0006, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0060}
    },
    "Stuff": {
        "35": {"hr_vs_adj": -0.0001, "bb_vs_adj": -0.0015, "k_vs_adj": -0.0726, "h_nothr_vs_adj":  0.0224},
        "40": {"hr_vs_adj": -0.0003, "bb_vs_adj": -0.0014, "k_vs_adj": -0.0395, "h_nothr_vs_adj":  0.0157},
        "45": {"hr_vs_adj":  0.0003, "bb_vs_adj":  0.0001, "k_vs_adj": -0.0154, "h_nothr_vs_adj":  0.0048},
        "50": {"hr_vs_adj":  0.0000, "bb_vs_adj":  0.0000, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0000},
        "55": {"hr_vs_adj":  0.0000, "bb_vs_adj": -0.0005, "k_vs_adj":  0.0310, "h_nothr_vs_adj": -0.0096},
        "60": {"hr_vs_adj": -0.0001, "bb_vs_adj": -0.0002, "k_vs_adj":  0.0478, "h_nothr_vs_adj": -0.0120},
        "65": {"hr_vs_adj": -0.0006, "bb_vs_adj": -0.0006, "k_vs_adj":  0.0565, "h_nothr_vs_adj": -0.0220},
        "70": {"hr_vs_adj": -0.0002, "bb_vs_adj": -0.0004, "k_vs_adj":  0.0752, "h_nothr_vs_adj": -0.0217},
        "75": {"hr_vs_adj": -0.0004, "bb_vs_adj": -0.0001, "k_vs_adj":  0.0881, "h_nothr_vs_adj": -0.0261},
        "80": {"hr_vs_adj": -0.0001, "bb_vs_adj": -0.0001, "k_vs_adj":  0.1081, "h_nothr_vs_adj": -0.0316}
    },
    "Stamina": {
        "40": {"hr_vs_adj": -0.0008, "bb_vs_adj": -0.0009, "k_vs_adj":  0.0007, "h_nothr_vs_adj":  0.0004},
        "45": {"hr_vs_adj": -0.0003, "bb_vs_adj": -0.0003, "k_vs_adj": -0.0001, "h_nothr_vs_adj":  0.0003},
        "50": {"hr_vs_adj":  0.0000, "bb_vs_adj":  0.0000, "k_vs_adj":  0.0000, "h_nothr_vs_adj":  0.0000},
        "55": {"hr_vs_adj":  0.0000, "bb_vs_adj": -0.0003, "k_vs_adj":  0.0009, "h_nothr_vs_adj": -0.0011},
        "60": {"hr_vs_adj":  0.0001, "bb_vs_adj": -0.0006, "k_vs_adj": -0.0003, "h_nothr_vs_adj":  0.0003}
    }
}


# ===============================================
# Hitting wOBA component adjustments by rating
# ===============================================

BATTING_COMPONENTS_ADJUST_MAP = {
    "babip": {
        "20": {"hr_pct_adj": -0.0002, "k_pct_adj": -0.0025, "bb_pct_adj": 0.0006, "1b_pct_adj": -0.0550, "2b_pct_adj": -0.0150, "3b_pct_adj": -0.0017},
        "25": {"hr_pct_adj":  0.0000, "k_pct_adj": -0.0009, "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0357, "2b_pct_adj": -0.0096, "3b_pct_adj": -0.0012},
        "30": {"hr_pct_adj": -0.0001, "k_pct_adj": -0.0019, "bb_pct_adj": -0.0004, "1b_pct_adj": -0.0284, "2b_pct_adj": -0.0077, "3b_pct_adj": -0.0010},
        "35": {"hr_pct_adj":  0.0000, "k_pct_adj": -0.0014, "bb_pct_adj": -0.0004, "1b_pct_adj": -0.0217, "2b_pct_adj": -0.0057, "3b_pct_adj": -0.0007},
        "40": {"hr_pct_adj": 0.0005, "k_pct_adj": -0.0005, "bb_pct_adj": -0.0001, "1b_pct_adj": -0.0139, "2b_pct_adj": -0.0041, "3b_pct_adj": -0.0004},
        "45": {"hr_pct_adj": 0.0006, "k_pct_adj": -0.0006, "bb_pct_adj": -0.0002, "1b_pct_adj": -0.0080, "2b_pct_adj": -0.0017, "3b_pct_adj":  0.0000},
        "50": {"hr_pct_adj": 0.0000, "k_pct_adj": 0.0000, "bb_pct_adj": 0.0000, "1b_pct_adj": 0.0000, "2b_pct_adj": 0.0000, "3b_pct_adj": 0.0000},
        "55": {"hr_pct_adj": 0.0001, "k_pct_adj": -0.0020, "bb_pct_adj": -0.0013, "1b_pct_adj":  0.0105, "2b_pct_adj":  0.0030, "3b_pct_adj":  0.0005},
        "60": {"hr_pct_adj": 0.0004, "k_pct_adj": -0.0022, "bb_pct_adj":  0.0064, "1b_pct_adj":  0.0149, "2b_pct_adj":  0.0044, "3b_pct_adj":  0.0005},
        "65": {"hr_pct_adj": 0.0004, "k_pct_adj": -0.0022, "bb_pct_adj":  0.0060, "1b_pct_adj":  0.0185, "2b_pct_adj":  0.0053, "3b_pct_adj":  0.0008},
        "70": {"hr_pct_adj": 0.0004, "k_pct_adj": -0.0039, "bb_pct_adj":  0.0070, "1b_pct_adj":  0.0224, "2b_pct_adj":  0.0061, "3b_pct_adj":  0.0009},
        "75": {"hr_pct_adj": -0.0003, "k_pct_adj": -0.0033, "bb_pct_adj":  0.0065, "1b_pct_adj":  0.0261, "2b_pct_adj":  0.0070, "3b_pct_adj":  0.0011},
        "80": {"hr_pct_adj": -0.0001, "k_pct_adj": -0.0019, "bb_pct_adj":  0.0110, "1b_pct_adj":  0.0321, "2b_pct_adj":  0.0104, "3b_pct_adj":  0.0011}
    },
    "avk": {
        "20": {"hr_pct_adj": 0.0001, "k_pct_adj": 0.2675, "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0634, "2b_pct_adj": -0.0185, "3b_pct_adj": -0.0021},
        "25": {"hr_pct_adj": -0.0004, "k_pct_adj": 0.1780, "bb_pct_adj": -0.0006, "1b_pct_adj": -0.0422, "2b_pct_adj": -0.0123, "3b_pct_adj": -0.0014},
        "30": {"hr_pct_adj": 0.0004, "k_pct_adj": 0.1484, "bb_pct_adj": -0.0009, "1b_pct_adj": -0.0353, "2b_pct_adj": -0.0100, "3b_pct_adj": -0.0013},
        "35": {"hr_pct_adj": 0.0003, "k_pct_adj": 0.1159, "bb_pct_adj": 0.0001, "1b_pct_adj": -0.0278, "2b_pct_adj": -0.0081, "3b_pct_adj": -0.0008},
        "40": {"hr_pct_adj": 0.0007, "k_pct_adj": 0.0835, "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0204, "2b_pct_adj": -0.0058, "3b_pct_adj": -0.0006},
        "45": {"hr_pct_adj": 0.0002, "k_pct_adj": 0.0408, "bb_pct_adj": -0.0001, "1b_pct_adj": -0.0092, "2b_pct_adj": -0.0032, "3b_pct_adj": 0.0000},
        "50": {"hr_pct_adj": 0.0000, "k_pct_adj": 0.0000, "bb_pct_adj": 0.0000, "1b_pct_adj": 0.0000, "2b_pct_adj": 0.0000, "3b_pct_adj": 0.0000},
        "55": {"hr_pct_adj": 0.0005, "k_pct_adj": -0.0435, "bb_pct_adj": -0.0006, "1b_pct_adj": 0.0095, "2b_pct_adj": 0.0031, "3b_pct_adj": 0.0004},
        "60": {"hr_pct_adj": 0.0006, "k_pct_adj": -0.0659, "bb_pct_adj": -0.0007, "1b_pct_adj": 0.0148, "2b_pct_adj": 0.0049, "3b_pct_adj": 0.0007},
        "65": {"hr_pct_adj": 0.0003, "k_pct_adj": -0.0836, "bb_pct_adj": 0.0061, "1b_pct_adj": 0.0169, "2b_pct_adj": 0.0052, "3b_pct_adj": 0.0007},
        "70": {"hr_pct_adj": 0.0004, "k_pct_adj": -0.1006, "bb_pct_adj": 0.0066, "1b_pct_adj": 0.0219, "2b_pct_adj": 0.0074, "3b_pct_adj": 0.0011},
        "75": {"hr_pct_adj": 0.0000, "k_pct_adj": -0.1113, "bb_pct_adj": 0.0063, "1b_pct_adj": 0.0243, "2b_pct_adj": 0.0071, "3b_pct_adj": 0.0011},
        "80": {"hr_pct_adj": 0.0001, "k_pct_adj": -0.1223, "bb_pct_adj": 0.0116, "1b_pct_adj": 0.0251, "2b_pct_adj": 0.0087, "3b_pct_adj": 0.0007}
    },
    "gap": {
        "20": {"hr_pct_adj": 0.0004, "k_pct_adj": -0.0007, "bb_pct_adj": -0.0001, "1b_pct_adj": 0.0363, "2b_pct_adj": -0.0355, "3b_pct_adj": -0.0041},
        "25": {"hr_pct_adj": -0.0001, "k_pct_adj": -0.0006, "bb_pct_adj": 0.0003, "1b_pct_adj": 0.0326, "2b_pct_adj": -0.0307, "3b_pct_adj": -0.0035},
        "30": {"hr_pct_adj": 0.0002, "k_pct_adj": -0.0009, "bb_pct_adj": -0.0005, "1b_pct_adj": 0.0273, "2b_pct_adj": -0.0246, "3b_pct_adj": -0.0029},
        "35": {"hr_pct_adj": -0.0002, "k_pct_adj": -0.0002, "bb_pct_adj": -0.0003, "1b_pct_adj": 0.0203, "2b_pct_adj": -0.0185, "3b_pct_adj": -0.0022},
        "40": {"hr_pct_adj": 0.0003, "k_pct_adj": -0.0004, "bb_pct_adj": 0.0007, "1b_pct_adj": 0.0139, "2b_pct_adj": -0.0136, "3b_pct_adj": -0.0013},
        "45": {"hr_pct_adj": 0.0006, "k_pct_adj": 0.0003,  "bb_pct_adj": -0.0002, "1b_pct_adj": 0.0060, "2b_pct_adj": -0.0064, "3b_pct_adj": -0.0005},
        "50": {"hr_pct_adj": 0.0000, "k_pct_adj": 0.0000, "bb_pct_adj": 0.0000, "1b_pct_adj": 0.0000, "2b_pct_adj": 0.0000, "3b_pct_adj": 0.0000},
        "55": {"hr_pct_adj": 0.0000, "k_pct_adj": 0.0000,  "bb_pct_adj": 0.0002, "1b_pct_adj": -0.0064, "2b_pct_adj": 0.0052, "3b_pct_adj": 0.0008},
        "60": {"hr_pct_adj": 0.0004, "k_pct_adj": 0.0009,  "bb_pct_adj": 0.0007, "1b_pct_adj": -0.0084, "2b_pct_adj": 0.0074, "3b_pct_adj": 0.0011},
        "65": {"hr_pct_adj": 0.0007, "k_pct_adj": 0.0006,  "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0111, "2b_pct_adj": 0.0097, "3b_pct_adj": 0.0011},
        "70": {"hr_pct_adj": 0.0006, "k_pct_adj": 0.0001,  "bb_pct_adj": -0.0008, "1b_pct_adj": -0.0129, "2b_pct_adj": 0.0126, "3b_pct_adj": 0.0016},
        "75": {"hr_pct_adj": 0.0003, "k_pct_adj": 0.0008,  "bb_pct_adj": 0.0002, "1b_pct_adj": -0.0144, "2b_pct_adj": 0.0134, "3b_pct_adj": 0.0017},
        "80": {"hr_pct_adj": 0.0001, "k_pct_adj": 0.0004, "bb_pct_adj": -0.0002, "1b_pct_adj": -0.0254, "2b_pct_adj": 0.0225, "3b_pct_adj": 0.0026}
    },
   "pow": {
        "20": {"hr_pct_adj": -0.0300, "k_pct_adj": -0.0009, "bb_pct_adj": -0.0006, "1b_pct_adj": 0.0058, "2b_pct_adj": 0.0017, "3b_pct_adj": 0.0002},
        "25": {"hr_pct_adj": -0.0276, "k_pct_adj": -0.0014, "bb_pct_adj": 0.0000, "1b_pct_adj": 0.0055, "2b_pct_adj": 0.0023, "3b_pct_adj": 0.0001},
        "30": {"hr_pct_adj": -0.0246, "k_pct_adj": -0.0013, "bb_pct_adj": -0.0006, "1b_pct_adj": 0.0035, "2b_pct_adj": 0.0016, "3b_pct_adj": 0.0003},
        "35": {"hr_pct_adj": -0.0195, "k_pct_adj": -0.0016, "bb_pct_adj": -0.0011, "1b_pct_adj": 0.0033, "2b_pct_adj": 0.0014, "3b_pct_adj": 0.0004},
        "40": {"hr_pct_adj": -0.0146, "k_pct_adj": -0.0005, "bb_pct_adj": -0.0006, "1b_pct_adj": 0.0023, "2b_pct_adj": 0.0002, "3b_pct_adj": 0.0004},
        "45": {"hr_pct_adj": -0.0070, "k_pct_adj":  0.0000, "bb_pct_adj": -0.0002, "1b_pct_adj": 0.0012, "2b_pct_adj": 0.0004, "3b_pct_adj": 0.0003},
        "50": {"hr_pct_adj": 0.0000, "k_pct_adj": 0.0000, "bb_pct_adj": 0.0000, "1b_pct_adj": 0.0000, "2b_pct_adj": 0.0000, "3b_pct_adj": 0.0000},
        "55": {"hr_pct_adj":  0.0156, "k_pct_adj":  0.0007, "bb_pct_adj":  0.0001, "1b_pct_adj": -0.0044, "2b_pct_adj": -0.0013, "3b_pct_adj": -0.0001},
        "60": {"hr_pct_adj":  0.0241, "k_pct_adj": -0.0004, "bb_pct_adj":  0.0074, "1b_pct_adj": -0.0088, "2b_pct_adj": -0.0013, "3b_pct_adj":  0.0000},
        "65": {"hr_pct_adj":  0.0302, "k_pct_adj":  0.0003, "bb_pct_adj":  0.0068, "1b_pct_adj": -0.0098, "2b_pct_adj": -0.0017, "3b_pct_adj": -0.0001},
        "70": {"hr_pct_adj":  0.0362, "k_pct_adj":  0.0003, "bb_pct_adj":  0.0077, "1b_pct_adj": -0.0113, "2b_pct_adj": -0.0019, "3b_pct_adj":  0.0000},
        "75": {"hr_pct_adj":  0.0406, "k_pct_adj":  0.0002, "bb_pct_adj":  0.0073, "1b_pct_adj": -0.0134, "2b_pct_adj": -0.0016, "3b_pct_adj": -0.0001},
        "80": {"hr_pct_adj":  0.0558, "k_pct_adj": -0.0024, "bb_pct_adj":  0.0220, "1b_pct_adj": -0.0184, "2b_pct_adj": -0.0044, "3b_pct_adj": -0.0003}
    },
    "eye": {
        "20": {"hr_pct_adj": 0.0026, "k_pct_adj": 0.0083, "bb_pct_adj": -0.0593, "1b_pct_adj": 0.0117, "2b_pct_adj": 0.0029, "3b_pct_adj": 0.0003},
        "25": {"hr_pct_adj": 0.0021, "k_pct_adj": 0.0078, "bb_pct_adj": -0.0548, "1b_pct_adj": 0.0106, "2b_pct_adj": 0.0028, "3b_pct_adj": 0.0003},
        "30": {"hr_pct_adj": 0.0019, "k_pct_adj": 0.0061, "bb_pct_adj": -0.0453, "1b_pct_adj": 0.0089, "2b_pct_adj": 0.0025, "3b_pct_adj": 0.0002},
        "35": {"hr_pct_adj":  0.0019, "k_pct_adj":  0.0054, "bb_pct_adj": -0.0355, "1b_pct_adj":  0.0061, "2b_pct_adj":  0.0017, "3b_pct_adj":  0.0005},
        "40": {"hr_pct_adj":  0.0013, "k_pct_adj":  0.0033, "bb_pct_adj": -0.0260, "1b_pct_adj":  0.0042, "2b_pct_adj":  0.0015, "3b_pct_adj":  0.0002},
        "45": {"hr_pct_adj":  0.0008, "k_pct_adj":  0.0018, "bb_pct_adj": -0.0117, "1b_pct_adj":  0.0020, "2b_pct_adj":  0.0004, "3b_pct_adj":  0.0003},
        "50": {"hr_pct_adj":  0.0000, "k_pct_adj":  0.0000, "bb_pct_adj":  0.0000, "1b_pct_adj":  0.0000, "2b_pct_adj":  0.0000, "3b_pct_adj":  0.0000},
        "55": {"hr_pct_adj": -0.0002, "k_pct_adj": -0.0011, "bb_pct_adj":  0.0376, "1b_pct_adj": -0.0026, "2b_pct_adj": -0.0008, "3b_pct_adj": -0.0001},
        "60": {"hr_pct_adj": -0.0005, "k_pct_adj": -0.0026, "bb_pct_adj":  0.0560, "1b_pct_adj": -0.0040, "2b_pct_adj": -0.0013, "3b_pct_adj": -0.0002},
        "65": {"hr_pct_adj": -0.0009, "k_pct_adj": -0.0034, "bb_pct_adj":  0.0640, "1b_pct_adj": -0.0047, "2b_pct_adj": -0.0016, "3b_pct_adj": -0.0002},
        "70": {"hr_pct_adj": -0.0017, "k_pct_adj": -0.0030, "bb_pct_adj":  0.0710, "1b_pct_adj": -0.0051, "2b_pct_adj": -0.0018, "3b_pct_adj": -0.0003},
        "75": {"hr_pct_adj": -0.0019, "k_pct_adj":  0.0001, "bb_pct_adj":  0.0406, "1b_pct_adj": -0.0085, "2b_pct_adj": -0.0031, "3b_pct_adj": -0.0001},
        "80": {"hr_pct_adj": -0.0026, "k_pct_adj": -0.0028, "bb_pct_adj":  0.0684, "1b_pct_adj": -0.0160, "2b_pct_adj": -0.0038, "3b_pct_adj": -0.0003}
    },
    "speed": {
        "40": {"hr_pct_adj": 0.0005, "k_pct_adj": 0.0005, "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0009, "2b_pct_adj": 0.0033, "3b_pct_adj": -0.0022},
        "45": {"hr_pct_adj": 0.0007, "k_pct_adj": 0.0015, "bb_pct_adj": -0.0007, "1b_pct_adj": -0.0017, "2b_pct_adj": 0.0011, "3b_pct_adj": -0.0012},
        "50": {"hr_pct_adj": 0.0004, "k_pct_adj": 0.0010, "bb_pct_adj": -0.0003, "1b_pct_adj": -0.0010, "2b_pct_adj": -0.0006, "3b_pct_adj": 0.0005},
        "55": {"hr_pct_adj": 0.0006, "k_pct_adj": 0.0011, "bb_pct_adj": 0.0001, "1b_pct_adj": -0.0015, "2b_pct_adj": -0.0015, "3b_pct_adj": 0.0011},
        "60": {"hr_pct_adj": 0.0006, "k_pct_adj": 0.0011, "bb_pct_adj": 0.0000, "1b_pct_adj": -0.0015, "2b_pct_adj": -0.0010, "3b_pct_adj": 0.0013},
        "65": {"hr_pct_adj": 0.0003, "k_pct_adj": 0.0002, "bb_pct_adj": -0.0004, "1b_pct_adj": -0.0008, "2b_pct_adj": -0.0011, "3b_pct_adj": 0.0013},
        "70": {"hr_pct_adj": 0.0003, "k_pct_adj": 0.0005, "bb_pct_adj": -0.0004, "1b_pct_adj": -0.0011, "2b_pct_adj": -0.0029, "3b_pct_adj": 0.0018},
        "75": {"hr_pct_adj": 0.0007, "k_pct_adj": 0.0002, "bb_pct_adj": -0.0003, "1b_pct_adj": -0.0008, "2b_pct_adj": -0.0019, "3b_pct_adj": 0.0021}
    }
}

# ===============================================
# Fielding run values vs replacement, by position
# ===============================================

FIELDING_RUN_VALUES_VS_REPLACEMENT = {
    "C": {
        "Cfram": {30: -8.6, 35: -6.0, 40: -6.1, 45: -2.7, 50: -1.4, 55: -1.2, 60: 0.0, 65: 7.2, 70: 8.8, 75: 10.7},
        "Cabil": {30: -7.8, 35: -6.9, 40: -6.0, 45: -5.1, 50: -4.2, 55: -0.7, 60: 0.0, 65: 0.7, 70: 1.5, 75: 2.2},
        "Carm":  {30: -14.7, 35: -1.2, 40: -1.2, 45: -1.2, 50: -0.4, 55: 0.0, 60: 0.4, 65: 0.7, 70: 1.1, 75: 1.4}
    },
    "CF": {
        "OFrange": {30: -24.4, 35: -24.4, 40: -24.4, 45: -24.4, 50: -24.4, 55: -24.3, 60: 0.0, 65: 13.5, 70: 15.4, 75: 16.0},
        "OFerror": {30: -3.9, 35: -3.8, 40: -3.7, 45: -3.5, 50: -3.4, 55: -2.9, 60: 0.0, 65: 0.8, 70: 1.5, 75: 2.3},
        "OFarm":   {30: -9.7, 35: -8.6, 40: -7.4, 45: -6.3, 50: -5.1, 55: 0.0, 60: 0.1, 65: 0.3, 70: 4.2, 75: 7.0}
    },
    "RF": {
        "OFrange": {30: -42.2, 35: -40.1, 40: -37.2, 45: -3.0, 50: -0.9, 55: 0.0, 60: 0.6, 65: 1.2, 70: 1.8, 75: 2.4},
        "OFerror": {30: -2.9, 35: -2.4, 40: -1.8, 45: -1.3, 50: -0.8, 55: 0.0, 60: 0.8, 65: 1.6, 70: 2.4, 75: 3.3},
        "OFarm":   {30: -7.0, 35: -5.6, 40: -4.2, 45: -2.7, 50: -1.3, 55: 0.0, 60: 2.4, 65: 6.4, 70: 7.3, 75: 7.4}
    },
    "LF": {
        "OFrange": {30: -18.8, 35: -17.1, 40: -15.4, 45: -13.7, 50: -0.4, 55: 0.0, 60: 0.4, 65: 0.9, 70: 1.3, 75: 1.7},
        "OFerror": {30: -7.1, 35: -2.1, 40: -1.5, 45: -0.9, 50: -0.3, 55: 0.0, 60: 0.3, 65: 0.6, 70: 0.9, 75: 1.2},
        "OFarm":   {30: -4.1, 35: -3.3, 40: -2.6, 45: -1.8, 50: -1.0, 55: 0.0, 60: 1.0, 65: 2.0, 70: 3.0, 75: 4.0}
    },
    "SS": {
        "IFrange": {30: -10.0, 35: -8.2, 40: -6.4, 45: -4.6, 50: -2.8, 55: -1.4, 60: 0.0, 65: 17.0, 70: 34.2, 75: 35.5},
        "IFerror": {30: -11.7, 35: -11.1, 40: -10.5, 45: -9.1, 50: -3.4, 55: -1.3, 60: 0.0, 65: 2.4, 70: 3.3, 75: 4.2},
        "IFarm":   {30: -6.9, 35: -5.8, 40: -4.9, 45: -2.7, 50: -1.8, 55: -0.8, 60: 0.0, 65: 0.8, 70: 1.5, 75: 2.3},
        "turnDP":  {30: -7.3, 35: -7.3, 40: -6.8, 45: -5.9, 50: -3.2, 55: 0.0, 60: 0.0, 65: 0.0, 70: 3.0, 75: 3.4}
    },
    "2B": {
        "IFrange": {30: -39.6, 35: -39.0, 40: -39.0, 45: -39.0, 50: -21.8, 55: 0.0, 60: 0.6, 65: 1.2, 70: 1.8, 75: 2.4},
        "IFerror": {30: -8.0, 35: -3.6, 40: -2.5, 45: -0.9, 50: 0.0, 55: 0.0, 60: 0.5, 65: 0.8, 70: 2.7, 75: 6.2},
        "IFarm":   {30: -17.9, 35: -15.6, 40: -13.3, 45: -10.0, 50: -3.2, 55: 0.0, 60: 7.0, 65: 9.2, 70: 9.3, 75: 13.5},
        "turnDP":  {30: -16.7, 35: -11.3, 40: -7.4, 45: -6.4, 50: -3.8, 55: 0.0, 60: 1.0, 65: 2.1, 70: 3.1, 75: 5.6}
    },
    "3B": {
        "IFrange": {30: -8.2, 35: -7.5, 40: -6.8, 45: -6.0, 50: -2.4, 55: 0.0, 60: 2.6, 65: 4.3, 70: 7.8, 75: 10.9},
        "IFerror": {30: -6.9, 35: -5.4, 40: -3.9, 45: -2.5, 50: -0.8, 55: 0.0, 60: 3.1, 65: 3.6, 70: 4.2, 75: 4.7},
        "IFarm":   {30: -3.4, 35: -2.8, 40: -2.3, 45: -1.7, 50: -1.2, 55: 0.0, 60: 4.3, 65: 9.2, 70: 11.0, 75: 12.8}
    },
    "1B": {
        "IFrange": {30: -9.8, 35: -3.1, 40: -1.5, 45: 0.0, 50: 1.5, 55: 1.5, 60: 2.4, 65: 3.3, 70: 4.2, 75: 5.1},
        "IFerror": {30: -1.8, 35: -1.4, 40: -0.9, 45: -0.5, 50: 0.0, 55: 0.0, 60: 0.6, 65: 1.2, 70: 1.9, 75: 3.1},
        "IFarm":   {30: 0.0, 35: 0.0, 40: 0.0, 45: 0.0, 50: 0.0, 55: 0.0, 60: 1.0, 65: 1.4, 70: 1.8, 75: 2.6}
    }
}

