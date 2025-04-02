const express = require("express");
const jwt = require("jsonwebtoken");

const app = express();
app.use(express.json());

const SECRET_KEY = "your_secret_key";

app.post("/login", (req, res) => {
  const { username } = req.body;
  const token = jwt.sign({ username }, SECRET_KEY, { expiresIn: "1h" });
  res.json({ token });
});

const verifyToken = (req, res, next) => {
  const token = req.headers["authorization"];
  if (!token) return res.status(403).send("Token required");
  try {
    req.user = jwt.verify(token, SECRET_KEY);
    next();
  } catch {
    res.status(403).send("Invalid token");
  }
};

app.get("/dashboard", verifyToken, (req, res) => {
  res.send(`Welcome ${req.user.username}`);
});

app.listen(3000, () => console.log("Server running on port 3000"));
