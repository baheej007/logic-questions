from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='World')

@app.route('/user/<name>')
def user(name):
    return render_template('indexhtml', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
