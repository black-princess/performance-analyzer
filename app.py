import streamlit as st
from src.resume_parser import extract_skills
from src.hackathon_analyzer import analyze_hackathons
from src.recommender import generate_recommendations

st.set_page_config(page_title="Hackathon Analyzer", layout="centered")
st.title("AI Hackathon Performance Analyzer")

resume_text = st.text_area("Paste your resume text")

if st.button("Analyze"):
    skills = extract_skills(resume_text)
    stats = analyze_hackathons("data/hackathons.csv")
    recs = generate_recommendations(skills, stats)

    st.subheader("Extracted Skills")
    st.write(skills)

    st.subheader("Hackathon Performance")
    st.write(stats)

    st.subheader("Recommendations")
    for r in recs:
        st.write("•", r)
