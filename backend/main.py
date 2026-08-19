from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd


# =========================
# Load Model
# =========================

model = joblib.load("house_price_model.pkl")


# =========================
# FastAPI App
# =========================

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Request Schema
# =========================

class PredictionRequest(BaseModel):

    location: str
    Status: str
    Transaction: str
    Furnishing: str
    facing: str
    Ownership: str

    Bathroom: float
    Balcony: float

    Carpet_Area_sqft: float
    Super_Area_sqft: float

    Car_Parking_Count: float

    Current_Floor: float
    Total_Floors: float

    Has_Main_Road: int
    Has_Garden_Park: int
    Has_Pool: int

    Society_Frequency: float


# =========================
# Root Endpoint
# =========================

@app.get("/")
def home():

    return {
        "message": "House Price Prediction API is running"
    }


# =========================
# Prediction Endpoint
# =========================

@app.post("/predict")
def predict(data: PredictionRequest):

    input_data = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_data)[0]

    return {
        "predicted_price": float(prediction)
    }