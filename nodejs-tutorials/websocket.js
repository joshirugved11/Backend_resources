const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new Server(server);

io.on("connection", (socket) => {
  console.log("User connected");
  socket.on("message", (msg) => {
    io.emit("message", msg);
  });
});

server.listen(3000, () => console.log("WebSocket running on port 3000"));
