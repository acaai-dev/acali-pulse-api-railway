
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS voor frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComfortInput(BaseModel):
    temperature: float
    co2: float
    presence: bool
    light_level: float

@app.post("/comfort")
def evaluate_comfort(data: ComfortInput):
    if data.co2 > 1000:
        return {"status": "uncomfortable", "recommendation": "increase ventilation"}
    elif data.temperature > 26:
        return {"status": "uncomfortable", "recommendation": "lower temperature"}
    else:
        return {"status": "comfortable", "recommendation": "none"}
