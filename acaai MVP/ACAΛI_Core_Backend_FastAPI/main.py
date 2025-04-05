
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from datetime import datetime

app = FastAPI()

# CORS instellen voor frontend verbinding
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/presets")
def get_presets():
    with open("presets.json", "r") as f:
        return json.load(f)

@app.post("/log")
async def log_action(request: Request):
    data = await request.json()
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now().isoformat()} - {json.dumps(data)}\n")
    return {"status": "logged"}
