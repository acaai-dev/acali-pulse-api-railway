
// ACAΛI Lambda UI – Frontend script (MVP)

// Simuleer een slider input (0–100)
const slider = document.getElementById("comfort-slider");
const feedbackBox = document.getElementById("feedback");

slider.addEventListener("input", () => {
  const sliderValue = parseInt(slider.value); // bv. 0 = koud, 100 = warm

  // Simuleer vertaling naar temperatuur (bv. 20–26°C)
  const temperature = 20 + (sliderValue / 100) * 6;
  const co2 = 950; // dummywaarde
  const presence = true;
  const light_level = 180; // dummywaarde

  const data = { temperature, co2, presence, light_level };

  // API-call naar ACAΛI Pulse
  fetch("http://localhost:8000/comfort", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  })
    .then(res => res.json())
    .then(result => {
      console.log("Comfortstatus:", result.status);
      console.log("Aanbeveling:", result.recommendation);
      feedbackBox.innerText = `Status: ${result.status} \nAanbeveling: ${result.recommendation}`;
    })
    .catch(err => {
      console.error("Fout bij API-call", err);
      feedbackBox.innerText = "Verbinding mislukt met Pulse API.";
    });
});
