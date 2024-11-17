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
    employes = ['ahmad', 'ali', 'mohammad', 'hassan', 'reza', 'mehdi', 'sara']
    return render_template('hello_world.html', employes=employes)


@app.route('/num')
def num():
    xs = [1, 2, 3, 4, 5]
    ys = [4, 5, 6, 7, 8]
    combined = zip(xs, ys)  # Combine xs and ys
    return render_template("num.html", combined=combined)

@app.route('/dict')
def dict():
    employees = {
        1: {'name': 'ahmad', 'age': 20},
        2: {'name': 'ali', 'age': 22},
        3: {'name': 'mohammad', 'age': 24},
        4: {'name': 'hassan', 'age': 26},
        5: {'name': 'reza', 'age': 28},
        6: {'name': 'mehdi', 'age': 30},
        7: {'name': 'sara', 'age': 32},
        8: {'name': 'sara', 'age': 32},
        9: {'name': 'sara', 'age': 32},
        10: {'name': 'ajmal', 'age': 45}
    }
    return render_template('dict.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
