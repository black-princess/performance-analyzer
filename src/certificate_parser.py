import pytesseract
import pdfplumber
from PIL import Image

KEYWORDS = {
    "Winner": 2,
    "Finalist": 1,
    "Participation": 0
}

def extract_text_from_certificate(file):
    text = ""

    if file.type == "application/pdf":
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    else:  # image
        image = Image.open(file)
        text = pytesseract.image_to_string(image)

    return text.lower()

def detect_result(file):
    text = extract_text_from_certificate(file)

    for key in KEYWORDS:
        if key.lower() in text:
            return key, KEYWORDS[key]

    return "Participation", 0
