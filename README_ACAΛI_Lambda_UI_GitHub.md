# ACAΛI Lambda UI – MVP

[![HTML](https://img.shields.io/badge/HTML-frontend-orange)]()
[![JavaScript](https://img.shields.io/badge/JS-dynamic-lightgrey)]()
[![Status](https://img.shields.io/badge/status-demo--live-brightgreen)]()

De **ACAΛI Lambda UI** is de frontendinterface van het ACAΛI-systeem. Deze minimalistische maar krachtige interface laat gebruikers comfortinstellingen aanpassen, presets activeren en sfeer aanpassen via een intuïtieve slider.

---

## 🌐 Live demo
🔗 [Lambda UI MVP](https://67ed8ee3b323d6254544b0a3--astounding-cajeta-8b413b.netlify.app/dashboard.html)

---

## 🧱 Functionaliteiten (MVP)
- Comfortslider: aanpasbaar gevoelstemperatuur-profiel
- Sferen: keuze uit vooraf ingestelde presets
- Gebruiksvriendelijke interface, geoptimaliseerd voor wandpaneel
- Basisstructuur voor uitbreidingen (ESG, profiel, voorkeuren)

---

## 🔌 API-koppeling (optioneel)
Wil je de UI verbinden met de ACAΛI Pulse API? Gebruik dan onderstaande fetch-call:

```js
fetch("http://localhost:8000/comfort", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    temperature: 24.5,
    co2: 750,
    presence: true,
    light_level: 180
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

> ⚠️ Zorg dat je de Pulse API lokaal of in de cloud hebt draaien (FastAPI backend)

---

## 📁 Structuur
```
acali-lambda-ui/
├── index.html
├── styles.css
├── script.js
```

---

## 🚧 Toekomstige uitbreidingen
- ESG Insights tab
- Zone-afhankelijk gedrag (context awareness)
- Gebruikersprofielen via Kosmos Watch of badge
- Live comfortfeedback via Pulse

---

© 2025 ACAΛI – Designing intelligent comfort.
