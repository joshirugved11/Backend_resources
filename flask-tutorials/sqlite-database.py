from flask import Flask, g
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/users')
def users():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return str(users)

if __name__ == '__main__':
    app.run(debug=True)
