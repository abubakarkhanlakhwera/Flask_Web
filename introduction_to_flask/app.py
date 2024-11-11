from flask import Flask

app = Flask(__name__) 

@app.route('/<route>')
def home(route):
    return  f'<h1>Welcome to the {route.title()} page!</h1>'

@app.route('/about')
def about():
    return '<h1>Welcome to the about page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)