import streamlit as st
import matplotlib.pyplot as plt
from src.resume_parser import extract_skills
from src.hackathon_analyzer import analyze_hackathons
from src.recommender import generate_recommendations

st.set_page_config(page_title="Hackathon Analyzer", layout="centered")
st.title("AI Hackathon Performance Analyzer")

resume_text = st.text_area("Paste your resume text")

if st.button("Analyze"):
    skills = extract_skills(resume_text)
    df, stats = analyze_hackathons("data/hackathons.csv")
    recs = generate_recommendations(skills.keys(), stats)

    st.subheader("Skill Strength (TF-IDF)")
    st.write(skills)

    st.subheader("Hackathon Performance")
    st.write(stats)

    st.subheader("Performance Trend")
    fig, ax = plt.subplots()
    ax.plot(df.index + 1, df["score"], marker="o")
    ax.set_xlabel("Hackathon Number")
    ax.set_ylabel("Performance Score")
    st.pyplot(fig)

    st.subheader("Recommendations")
    for r in recs:
        st.write("•", r)
