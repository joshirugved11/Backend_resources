from flask import Flask, request

app = Flask(__name__)

@app.before_request
def before_request():
    print(f"Incoming request: {request.method} {request.path}")

@app.after_request
def after_request(response):
    print(f"Outgoing response: {response.status}")
    return response

@app.route('/')
def home():
    return "Middleware Example!"

if __name__ == '__main__':
    app.run(debug=True)
