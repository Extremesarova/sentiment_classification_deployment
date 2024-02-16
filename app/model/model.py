import pickle
from pathlib import Path

import pgzip

__version__ = "0.4.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with pgzip.open(f"{BASE_DIR}/tfidf_vectorizer_{__version__}.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)

with pgzip.open(f"{BASE_DIR}/logreg_classifier_{__version__}.pkl", "rb") as f:
    logreg_classifier = pickle.load(f)


def predict_sentiment(text: str) -> dict:
    vectorized_text = tfidf_vectorizer.transform([text])
    pred = logreg_classifier.predict_proba(vectorized_text)[0]

    return dict(zip(logreg_classifier.classes_, pred))
