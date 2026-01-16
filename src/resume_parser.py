def extract_skills(resume_text):
    skills = [
        "python", "machine learning", "deep learning",
        "nlp", "data analysis", "git"
    ]
    resume_text = resume_text.lower()
    return [skill for skill in skills if skill in resume_text]
