from flask import Flask, jsonify, render_template
from database import db
from models.post import Worker, Employee

app = Flask(__name__)

# Database configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'qwerty.'
MYSQL_DB = 'ayesha'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database with the app
db.init_app(app)

# Routes
@app.route('/get', methods=['GET', 'POST'])
def get():
    with app.app_context():
        # Add a new employee to the database
        new_employee = Employee(name='John Doe', age=30, salary=50000, city='NY', country='USA')
        db.session.add(new_employee)
        db.session.commit()

        # Fetch all data
        gets = Worker.query.all()
        employees = Employee.query.all()

    return render_template('index.html', gets=gets, employees=employees)


# Create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
