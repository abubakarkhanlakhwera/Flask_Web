from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the home page!</h1>'

@app.route('/check_score/<int:score>')
def check_score(score):
    if score >= 50:
        time.sleep(5)
        return redirect(url_for('pass_page'))
    else:
        return redirect(url_for('fail_page'))

# Rename the pass route to avoid using a reserved keyword
@app.route('/passed')
def pass_page():
    return '<h1>Congratulations! You passed!</h1>'

@app.route('/fail')
def fail_page():
    return '<h1>Oh no! You failed!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
