
# ACAΛI Core API (FastAPI)

## Beschrijving
Dit is een eenvoudige backend voor ACAΛI die:
- Preset-configuraties ophaalt via `/presets`
- Acties logt via `/log`

## Starten

1. Installeer vereisten:
```
pip install fastapi uvicorn
```

2. Start de server:
```
uvicorn main:app --reload
```

3. Open in je browser:
- [http://127.0.0.1:8000/presets](http://127.0.0.1:8000/presets)
- Logs worden opgeslagen in `log.txt`

