from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            Name: <input type="text" name="name">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)