# ACAΛI Core Backend

Deze eenvoudige FastAPI-server ontvangt preset- en temperatuurdata van de Lambda UI.

## Installatie

```bash
pip install -r requirements.txt
```

## Start de server

```bash
uvicorn main:app --reload
```

## Endpoints

- POST `/preset` – JSON: `{ "preset": "Focus" }`
- POST `/temperature` – JSON: `{ "value": 22.5 }`
