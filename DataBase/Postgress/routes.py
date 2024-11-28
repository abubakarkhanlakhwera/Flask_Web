from flask import render_template,request
from models.models import Person

def register_routes(app,db):
    @app.route('/',methods=['GET','POST'])
    def index():
        if request.method == "GET":
            employees = Person.query.all()
            return render_template('index.html',employees=employees)
        elif request.method == "POST":
            name = request.form.get('name')
            desig = request.form.get('design')
            scale = int(request.form.get('scale'))
            salary = int(request.form.get('salary'))
            wy = int(request.form.get('wy'))
            
            employee = Person(name=name,designation=desig,scale=scale,salary=salary, working_year_in_company=wy)
            
            db.session.add(employee)
            db.session.commit()
            
            employees = Person.query.all()
            return render_template('index.html',employees=employees)
