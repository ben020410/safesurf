document.getElementById("linkForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const link = document.getElementById("linkInput").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ link: link })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent = `Prediction: ${data.prediction}`;
    })
    .catch(error => console.error("Error:", error));
});
