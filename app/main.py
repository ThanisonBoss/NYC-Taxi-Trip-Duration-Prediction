from fastapi import FastAPI
from pydantic import BaseModel
import mlflow
import pandas as pd

app = FastAPI()

class PredictionRequest(BaseModel):
    PULocationID: float
    DOLocationID: float
    trip_distance: float

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def duration_predict(request: PredictionRequest):
    df_features = pd.DataFrame([request.dict()])
    mlflow.set_tracking_uri('http://mlflow:5000')
    model = mlflow.sklearn.load_model(model_uri=f"models:/duration_predict/Production")
    predict = round(model.predict(df_features)[0],2)
    return {"duration_predict": predict}


