import pickle
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/TfIdfLogRegSentiment-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)


def predict_sentiment(text: str) -> dict:
    pred = model.predict_proba([text])[0]

    return dict(zip(model.classes_, pred))
