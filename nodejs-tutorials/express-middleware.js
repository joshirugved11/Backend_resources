const express = require("express");
const app = express();

// Middleware function
app.use((req, res, next) => {
  console.log(`Request received: ${req.method} ${req.url}`);
  next();
});

app.get("/", (req, res) => res.send("Middleware Example"));

app.listen(3000, () => console.log("Server running on port 3000"));
