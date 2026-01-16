def generate_recommendations(skills, stats):
    recs = []

    if stats["Failures"] > stats["Wins"]:
        recs.append("Improve problem understanding and execution strategy.")

    if "git" not in skills:
        recs.append("Strengthen Git/GitHub usage for team collaboration.")

    if "machine learning" in skills and stats["Wins"] == 0:
        recs.append("Apply ML knowledge to real-world problem statements.")

    return recs
