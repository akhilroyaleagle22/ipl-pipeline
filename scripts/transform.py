import pandas as pd

def transform_matches(df):
    print("Transforming matches...")

    df = df.dropna(subset=["winner"]).copy()

    #clean date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    #Extract year from season (some seasons are "2007/08" format)
    df["season_year"] = df["season"].astype(str).str[:4].astype(int)

    #keep only the columns we actually need 
    df = df[[
        "matchId", "season", "season_year", "date", "venue", "city",
        "team1", "team2", "toss_winner", "toss_decision",
        "winner", "winner_runs", "winner_wickets",
        "player_of_match", "method", "outcome"
    ]]

    #reset index cleanly
    df = df.reset_index(drop=True)

    print(f"Transformed matches: {len(df)} rows")
    return df

def transform_deliveries(df):
    print("transforming deliveries...")

    df = df.rename(columns={
        "isWide": "is_wide",
        "isNoBall": "is_no_ball",
        "Byes": "byes",
        "LegByes": "leg_byes",
        "Penalty": "penalty"
    })

    #Fill NaN extras with 0
    df["is_wide"] = df["is_wide"].fillna(0)
    df["is_no_ball"] = df["is_no_ball"].fillna(0)
    df["byes"] = df["byes"].fillna(0)
    df["leg_byes"] = df["leg_byes"].fillna(0)
    df["penalty"] = df["penalty"].fillna(0)

    #calculate total runs per ball
    df["total_runs"] = (
        df["batsman_runs"] +
        df["extras"]
    )

    #flag valid balls (not wide, not no ball) for strike rate calculations
    df["is_valid_ball"] = (df["is_wide"] == 0) & (df["is_no_ball"] == 0)

    #clean date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Keep only columns we need
    df = df[[
        "matchId", "inning", "over", "ball", "date",
        "batting_team", "bowling_team",
        "batsman", "non_striker", "bowler",
        "batsman_runs", "extras", "total_runs",
        "is_wide", "is_no_ball", "is_valid_ball",
        "dismissal_kind", "player_dismissed"
    ]]

    df = df.reset_index(drop=True)

    print(f"Transformed deliveries: {len(df)} rows")
    return df


    