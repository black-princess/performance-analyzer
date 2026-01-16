import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer

SKILLS = [
    "python", "machine learning", "deep learning",
    "nlp", "data analysis", "git"
]

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def extract_skills_from_pdf(pdf_file):
    text = extract_text_from_pdf(pdf_file)

    vectorizer = TfidfVectorizer(vocabulary=SKILLS)
    tfidf = vectorizer.fit_transform([text])

    scores = dict(zip(
        vectorizer.get_feature_names_out(),
        tfidf.toarray()[0]
    ))

    return {k: round(v, 2) for k, v in scores.items() if v > 0}
