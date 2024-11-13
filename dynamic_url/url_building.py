from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the home page!</h1>'

@app.route('/check_score/<name>/<int:score>')
def check_score(name,score):
    if score >= 50:
        time.sleep(5)
        return redirect(url_for('pass_page',sname=name,marks=score))
    else:
        return redirect(url_for('fail_page',sname=name,marks=score))


@app.route('/passed/<sname>/<int:marks>')
def pass_page(sname,marks):
    return f'<h1>Congratulations {sname.title()}! You passed! Your marks are {marks}</h1>'

@app.route('/fail/<sname>/<int:marks>')
def fail_page(sname,marks):
    return f'<h1>Oh no {sname.title()}! You failed! Your marks are {marks}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
