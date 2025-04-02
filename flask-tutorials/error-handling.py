from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return "Page Not Found!", 404

if __name__ == '__main__':
    app.run(debug=True)
