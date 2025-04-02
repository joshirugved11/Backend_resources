from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    socketio.send(f'Echo: {message}')

if __name__ == '__main__':
    socketio.run(app, debug=True)
