from flask import Flask

app = Flask(__name__)

@app.route('/<route>')
def home(route):
    return f'<h1>Welcome to the {route.title()} page!</h1>'

@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1, num2):
    return f'<h1>Input was {num1} and {num2} and the sum is {num1 + num2}</h1>'

@app.route('/about')
def about():
    return '<h1>Welcome to the about page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)