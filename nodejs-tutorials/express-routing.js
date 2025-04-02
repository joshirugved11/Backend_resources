const express = require("express");
const app = express();

app.get("/", (req, res) => res.send("Welcome!"));
app.get("/about", (req, res) => res.send("About Page"));
app.get("/contact", (req, res) => res.send("Contact Page"));

app.listen(3000, () => console.log("Server running on port 3000"));
