def generate_recommendations(skills, stats):
    recs = []

    if stats["Failures"] > stats["Wins"]:
        recs.append(
            "You participate actively but struggle to convert ideas into winning solutions."
        )

    if "git" not in skills:
        recs.append(
            "Your resume lacks version control skills, which are crucial in team hackathons."
        )

    if "machine learning" in skills and stats["Wins"] == 0:
        recs.append(
            "You have ML knowledge, but hackathon outcomes suggest difficulty applying it under time constraints."
        )

    if len(skills) < 3:
        recs.append(
            "Your resume reflects limited technical breadth. Consider expanding project diversity."
        )

    return recs
def generate_summary(stats):
    if stats["Wins"] >= 2:
        return "You show strong competitive consistency and the ability to deliver under pressure."
    elif stats["Finalists"] >= 2:
        return "You are close to top-tier performance but need sharper execution."
    else:
        return "You are in an early growth phase and should focus on fundamentals and teamwork."
