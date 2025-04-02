const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: { user: "your-email@gmail.com", pass: "your-password" },
});

const mailOptions = {
  from: "your-email@gmail.com",
  to: "receiver@example.com",
  subject: "Hello from Node.js",
  text: "This is a test email",
};

transporter.sendMail(mailOptions, (err, info) => {
  if (err) console.error(err);
  else console.log("Email sent: " + info.response);
});
