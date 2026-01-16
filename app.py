import streamlit as st
import matplotlib.pyplot as plt

from src.resume_parser import extract_skills_from_pdf
from src.certificate_parser import detect_result
from src.recommender import generate_summary


st.set_page_config(page_title="Hackathon Analyzer", layout="centered")
st.title("AI Hackathon Performance Analyzer")

# 📄 Resume upload
resume_pdf = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# 🏅 Certificate upload
certificate_files = st.file_uploader(
    "Upload Hackathon Certificates (PDF / JPG)",
    type=["pdf", "jpg", "png"],
    accept_multiple_files=True
)

if st.button("Analyze"):

    # ✅ Validation
    if resume_pdf is None or not certificate_files:
        st.warning("Please upload both resume and certificates.")
        st.stop()

    # 1️⃣ Extract skills from resume
    skills = extract_skills_from_pdf(resume_pdf)

    # 2️⃣ Extract results from certificates
    scores = []
    for cert in certificate_files:
        result, score = detect_result(cert)
        scores.append(score)

    # 3️⃣ Stats
    stats = {
        "Total Hackathons": len(scores),
        "Wins": scores.count(2),
        "Finalists": scores.count(1),
        "Participations": scores.count(0)
    }

    # 📊 PERFORMANCE GRAPH (STEP 3.4)
    st.subheader("Hackathon Performance Trend")
    fig, ax = plt.subplots()
    ax.plot(range(1, len(scores) + 1), scores, marker="o")
    ax.set_xlabel("Hackathon Number")
    ax.set_ylabel("Performance Score")
    ax.set_yticks([0, 1, 2])
    ax.set_yticklabels(["Participation", "Finalist", "Winner"])
    st.pyplot(fig)

    # 🧠 Skills
    st.subheader("Extracted Skills (from Resume)")
    st.write(skills)

    # 📝 AI Summary
    summary = generate_summary(stats)
    st.subheader("AI Performance Summary")
    st.success(summary)
