const express = require("express");
const path = require("path");
const app = express();
const port = 3000;

app.use(express.static(__dirname));
app.use(express.json());

app.post("/submit", (req, res) => {
  const { name, email } = req.body;
  console.log(`Received: ${name}, ${email}`);
  // Send data to Flask backend
  fetch("http://backend:5000/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name, email })
  })
    .then(response => response.json())
    .then(data => res.json(data))
    .catch(error => res.status(500).json({ error: "Failed to submit data" }));
});

app.get("/submit", (req, res) => {
  res.status(200).json({ message: "Please use POST method to submit data to this endpoint." });
});

app.listen(port, () => {
  console.log(`Frontend listening at http://localhost:${port}`);
});

app.get("/",(req,res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});