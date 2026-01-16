import pandas as pd

def analyze_hackathons(csv_path):
    df = pd.read_csv(csv_path)

    result_score = {
        "Failed Prelims": 0,
        "Finalist": 1,
        "Winner": 2
    }

    df["score"] = df["result"].map(result_score)

    stats = {
        "Total Hackathons": len(df),
        "Wins": (df["result"] == "Winner").sum(),
        "Finalists": (df["result"] == "Finalist").sum(),
        "Failures": (df["result"] == "Failed Prelims").sum()
    }

    return df, stats

