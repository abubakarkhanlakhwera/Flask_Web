from flask import Flask, jsonify, render_template
from database import db
from models.post import Post
import random

# Initialize Flask app
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
@app.route('/random_number')
def random_number():
    number = random.randint(1, 100)
    return jsonify({'random_number': number})

@app.route('/add_post', methods=['GET'])
def add_post():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

# Create database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
