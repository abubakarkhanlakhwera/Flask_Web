from flask import Flask, render_template, redirect, url_for, flash , session , request
from forms import LoginForm
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    if "username" not in session:
        flash("Login Required")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {session['username']} , Welcome to About Page")
    return render_template('about.html')

@app.route('/contact')
def contact():
    if "username" not in session:
        flash("Login Required")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {session['username']} , Welcome to Contact Page")
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()   
    if form.validate_on_submit():
        session['username'] = form.username.data
        flash(f"Login Successful as {session['username'].title()}!")      
        next_url = request.args.get('next')
        return redirect(next_url or url_for('home'))
    
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    

