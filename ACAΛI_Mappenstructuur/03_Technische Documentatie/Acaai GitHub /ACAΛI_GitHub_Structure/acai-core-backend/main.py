
from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class PresetRequest(BaseModel):
    preset: str

class TemperatureRequest(BaseModel):
    value: float

@app.post("/preset")
async def set_preset(data: PresetRequest):
    print(f"[{datetime.now()}] Preset ontvangen: {data.preset}")
    return {"status": "ok", "received": data.preset}

@app.post("/temperature")
async def set_temperature(data: TemperatureRequest):
    print(f"[{datetime.now()}] Temperatuur ontvangen: {data.value} °C")
    return {"status": "ok", "received": data.value}
