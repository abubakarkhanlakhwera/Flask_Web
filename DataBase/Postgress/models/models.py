from app import db

class Person(db.Model):
    __tablename__ = 'Employee'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text, nullable = False)
    designation = db.Column(db.Text, nullable = False)
    scale = db.Column(db.Integer, nullable = False)
    working_year_in_company = db.Column(db.Integer, nullable = False)
    salary = db.Column(db.Integer, nullable = False)
    
    def bonus(self):
        bonus_pay = self.scale *  self.salary * 0.025 
        return bonus_pay
    
    def __repr__(self):
        return f'{self.name} has {self.bonus()} increment in his salary {self.salary} '
    
    