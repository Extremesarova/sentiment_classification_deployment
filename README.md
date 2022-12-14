# Sentiment Classifier Deployment with FastAPI and Docker

## 0. Clone this repository

And change the directory:

```bash
git clone https://github.com/Extremesarova/sentiment_classification_deployment.git
cd sentiment_classification_deployment
```

## 1. Download the model

With this [link](https://disk.yandex.ru/d/1ImXpmv0ZUftxA) and place it inside `/app/model` directory.

## 2. Create Docker container

```bash
docker build -t sentiment_classification-app:0.1.0 .
docker run -p 80:80 sentiment_classification-app:0.1.0
```

## 3. Open browser

With this link [http://0.0.0.0:80](http://0.0.0.0:80) to check that everything is okay:

```json
{"health_check":"OK","model_version":"0.1.0"}
```

To get the prediction:

1. Open webpage using this link [0.0.0.0/docs/predict](http://0.0.0.0/docs#/default/predict_predict_post).
2. Press "Try it out".
3. Replace `string` inside the form with your text containing sentiment in Russian:

    ```json
    {
    "text": "string"
    }
    ```

4. Press execute.
5. Look at the result below:

    ```json
    {
    "sentiment": {
        "negative": 0.13412402064162648,
        "neutral": 0.2727429156861964,
        "positive": 0.5931330636721771
        }
    }
    ```

Or just send a POST request using CURL like the one below in your terminal, replacing `string` with your text containing sentiment in Russian:

```bash
curl -X 'POST' \
  'http://0.0.0.0/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "string"
}'
```
