from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:qwerty.@localhost/ayesha'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ayesha.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://:password@localhost/dbname'
    
    db.init_app(app)
    
    
    from routes import register_routes
    register_routes(app,db)
    
    migrate = Migrate(app,db)
    return app