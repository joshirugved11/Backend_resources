const express = require("express");
const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/testdb", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const UserSchema = new mongoose.Schema({ name: String });
const User = mongoose.model("User", UserSchema);

const app = express();
app.use(express.json());

app.post("/users", async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.send(user);
});

app.listen(3000, () => console.log("Server running on port 3000"));
