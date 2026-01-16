import pandas as pd

def analyze_hackathons(csv_path):
    df = pd.read_csv(csv_path)

    total = len(df)
    wins = len(df[df["result"] == "Winner"])
    finalists = len(df[df["result"] == "Finalist"])
    failures = total - wins - finalists

    return {
        "Total Hackathons": total,
        "Wins": wins,
        "Finalists": finalists,
        "Failures": failures
    }
