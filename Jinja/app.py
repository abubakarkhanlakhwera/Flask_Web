from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    birthdate_str = request.form['birthdate']
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    
    # Calculate age
    age_ = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return render_template('result.html', age=age_,)
@app.route('/h')
def hello_world():
    return render_template('hello_world.html')
if __name__ == '__main__':
    app.run(debug=True)
