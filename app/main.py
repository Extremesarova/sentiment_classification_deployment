from fastapi import FastAPI
from pydantic import BaseModel

from app.model.model import __version__ as model_version
from app.model.model import predict_sentiment

app = FastAPI()


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    sentiment: dict


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(input_text: TextIn):
    sentiment = predict_sentiment(input_text.text)

    return {"sentiment": sentiment}
