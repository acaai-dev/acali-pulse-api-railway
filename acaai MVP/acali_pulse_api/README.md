# ACAΛI Pulse API – MVP

Een eenvoudige FastAPI backend voor het evalueren van comfortparameters in het ACAΛI-systeem.

## Starten
1. Installeer dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start de server:
   ```
   uvicorn app.main:app --reload
   ```

## Endpoint
- POST `/comfort`
  ```json
  {
    "temperature": 24.5,
    "co2": 800,
    "presence": true,
    "light_level": 180
  }
  ```
