import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def preprocess(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z0-9 ]","",text)
    text = text.split()
    text = [word for word in text if word not in ENGLISH_STOP_WORDS]
    text = " ".join(text)
    return text

def preprocess_text(texts):
    return [preprocess(text)for text in texts]