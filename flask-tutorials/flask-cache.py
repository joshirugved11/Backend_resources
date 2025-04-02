from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route('/expensive')
@cache.cached(timeout=10)  # Cache result for 10 seconds
def expensive():
    import time
    time.sleep(5)  # Simulate a slow response
    return "This is a slow response, but now cached!"

if __name__ == '__main__':
    app.run(debug=True)
