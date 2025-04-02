from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['username']
        return redirect(url_for('dashboard'))
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome {session['user']}!"
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
