from flask import Flask, redirect, url_for
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'random_secret_key'
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    client_kwargs={'scope': 'openid email profile'}
)

@app.route('/login')
def login():
    return google.authorize_redirect(url_for('callback', _external=True))

@app.route('/callback')
def callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    return f"Hello, {user_info['name']}!"

if __name__ == '__main__':
    app.run(debug=True)
