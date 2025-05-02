import pandas as pd
from pathlib import Path
from config import (
    filepath,
    club_lookup,
    PLAYERS_COLUMNS,
    PLAYERS_COLUMN_RENAMES,
    PITCHING_STATS_COLUMNS,
    SCOUTED_RATINGS_COLUMNS,
    PITCH_RATING_COLUMNS,
    POTENTIAL_PITCH_RATING_COLUMNS,
    SCOUTED_RATINGS_RENAMES,
    rename_columns,
    ID,
    PITCH_MINIMUM_RATING,
    HITTING_STATS_COLUMNS,
    POSITION_THRESHOLDS,
    pistachio_filepath,
)

def load_players() -> pd.DataFrame:
    file = filepath / 'players.csv'
    df = pd.read_csv(file, usecols=PLAYERS_COLUMNS, low_memory=False)
    # Remove retired players
    df = df[df.retired != 1]
    df = df.drop(columns=["retired"])
    # Rename columns
    for old, new in PLAYERS_COLUMN_RENAMES.items():
        df = rename_columns(df, old, new)
    # Combine first and last name into a single 'name' column
    df["name"] = df["first_name"] + " " + df["last_name"]
    df = df.drop(columns=["first_name", "last_name"])    
    # Map numeric org values to team abbreviations using the club lookup
    # first flag minor leaguers for whom team and organisaition IDs are different
    df["minor"] = (df["org"] != df["team_id"]).astype(int)
    df["org"] = df["org"].map(club_lookup)
    # map numeric organization_id to abbreviation
    return df

def add_pitching_career_stats(df: pd.DataFrame) -> pd.DataFrame:
    file = filepath / 'players_career_pitching_stats.csv'
    pitching_stats_df = pd.read_csv(file, usecols=PITCHING_STATS_COLUMNS, low_memory=False)
    # Filter for MLB + combined L/R splits, and most recent season only
    pitching_stats_df = pitching_stats_df[
        (pitching_stats_df['level_id'] == 1) & 
        (pitching_stats_df['split_id'] == 1)
    ]
    max_year = pitching_stats_df['year'].max()
    pitching_stats_df = pitching_stats_df[pitching_stats_df['year'] == max_year]
    # sum innings pitched by player_id and merge into main DataFrame
    pitching_stats_df = pitching_stats_df.groupby('player_id')[['ip']].sum().reset_index()
    df = pd.merge(df, pitching_stats_df, on='player_id', how='left')
    df['ip'] = df['ip'].fillna(0).astype(int)
    return df

def add_hitting_career_stats(df: pd.DataFrame) -> pd.DataFrame:
    file = filepath / 'players_career_batting_stats.csv'
    hitting_stats_df = pd.read_csv(file, usecols=HITTING_STATS_COLUMNS, low_memory=False)
    # Filter for MLB + combined L/R splits, and most recent season only
    hitting_stats_df = hitting_stats_df[
        (hitting_stats_df['level_id'] == 1) & 
        (hitting_stats_df['split_id'] == 1)
    ]
    max_year = hitting_stats_df['year'].max()
    hitting_stats_df = hitting_stats_df[hitting_stats_df['year'] == max_year]
    # sum plate appearances by player_id and merge into main DataFrame
    hitting_stats_df = hitting_stats_df.groupby('player_id')[['pa']].sum().reset_index()
    df = pd.merge(df, hitting_stats_df, on='player_id', how='left')
    df['pa'] = df['pa'].fillna(0).astype(int)
    return df

def add_scouted_ratings(df: pd.DataFrame) -> pd.DataFrame:
    file = filepath / 'players_scouted_ratings.csv'
    all_rating_columns = SCOUTED_RATINGS_COLUMNS + PITCH_RATING_COLUMNS + POTENTIAL_PITCH_RATING_COLUMNS
    ratings_df = pd.read_csv(file, usecols=all_rating_columns, low_memory=False)
    # Keep only ratings from your scouting director
    ratings_df = ratings_df[ratings_df['scouting_coach_id'] == ID]
    ratings_df = ratings_df.drop(columns=["scouting_coach_id"])
    # Rename the column for clarity
    for old, new in SCOUTED_RATINGS_RENAMES.items():
        ratings_df = rename_columns(ratings_df, old, new)
    df = pd.merge(df, ratings_df, on="player_id", how="left")
    return df

# count 'how many pitches' a pitcher has got based on minimum threshold ratings
def count_pitches(df: pd.DataFrame) -> pd.DataFrame:
    pitch_flags = df[PITCH_RATING_COLUMNS] >= PITCH_MINIMUM_RATING
    df["pitches"] = pitch_flags.astype(int).sum(axis=1)
    potential_pitch_flags = df[POTENTIAL_PITCH_RATING_COLUMNS] >= PITCH_MINIMUM_RATING
    df["pitchesP"] = potential_pitch_flags.astype(int).sum(axis=1)
    df = df.drop(columns=PITCH_RATING_COLUMNS)
    df = df.drop(columns=POTENTIAL_PITCH_RATING_COLUMNS)
    return df

# determine whether a player 'can field' at a given position based on minimum threshold ratings
def can_field(df: pd.DataFrame) -> pd.DataFrame:
    def evaluate_row(row):
        positions = []
        for pos, checks in POSITION_THRESHOLDS.items():
            if all(row.get(col, 0) >= threshold for col, threshold in checks):
                positions.append(pos)
        return ", ".join(positions)

    df["field"] = df.apply(evaluate_row, axis=1)
    return df

# Add a flag column for names listed in flagged.txt
import numpy as np
def is_flagged(df: pd.DataFrame) -> pd.DataFrame:
    # Read player_ids from text file and convert to integers
    with open(pistachio_filepath / 'flagged.txt', 'r') as f:
        flagged_ids = [int(line.strip()) for line in f if line.strip().isdigit()]

    # Add 'flag' column based on player_id match
    df["flag"] = np.where(df["player_id"].isin(flagged_ids), "flag", "")
    return df