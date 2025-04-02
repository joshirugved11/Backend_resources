from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_password'

mail = Mail(app)

@app.route('/send_email/<email>')
def send_email(email):
    msg = Message("Hello from Flask", sender="your_email@gmail.com", recipients=[email])
    msg.body = "This is a test email from Flask!"
    mail.send(msg)
    return f"Email sent to {email}!"

if __name__ == '__main__':
    app.run(debug=True)
