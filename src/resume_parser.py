from sklearn.feature_extraction.text import TfidfVectorizer

SKILLS = [
    "python", "machine learning", "deep learning",
    "nlp", "data analysis", "git"
]

def extract_skills(resume_text):
    vectorizer = TfidfVectorizer(vocabulary=SKILLS)
    tfidf_matrix = vectorizer.fit_transform([resume_text.lower()])
    
    scores = dict(zip(vectorizer.get_feature_names_out(),
                      tfidf_matrix.toarray()[0]))
    
    found_skills = {k: round(v, 2) for k, v in scores.items() if v > 0}
    return found_skills
