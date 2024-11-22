from database import db

class Worker(db.Model):
    __tablename__ = 'get'  # Optional: Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)  # Default value
    email = db.Column(db.String(100))  # Updated to consistent lowercase naming

    def __repr__(self):
        return f"<GET {self.name}, Active: {self.is_active}>"

class Employee(db.Model):
    __tablename__ = 'employee'  # Optional: Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def __repr__(self):
        return f"<Employee {self.name}, Salary: {self.salary}>"
