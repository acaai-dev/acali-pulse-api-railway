
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ACAΛI Pulse API – MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SensorData(BaseModel):
    temperature: float
    co2: int
    presence: bool
    light_level: Optional[int] = None

@app.post("/comfort")
def evaluate_comfort(data: SensorData):
    response = {
        "status": "stable",
        "recommendation": "no change"
    }

    if data.presence and data.co2 > 900:
        response["status"] = "uncomfortable"
        response["recommendation"] = "increase ventilation"
    elif data.temperature > 25:
        response["status"] = "warm"
        response["recommendation"] = "lower temperature"
    elif data.light_level is not None and data.light_level < 200:
        response["status"] = "dark"
        response["recommendation"] = "increase lighting"

    return response
