from flask import Flask, render_template, redirect, url_for, flash ,  request, make_response
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    username  = request.cookies.get('username')
    if username is None:
        flash("Login Required")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {username} , Welcome to About Page")
    return render_template('about.html')

@app.route('/contact')
def contact():
    username  = request.cookies.get('username')
    if username is None:
        flash("Login Required")
        return redirect(url_for('login', next=request.url))
    else:
        flash(f"Hi {username} , Welcome to Contact Page")
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()   
    if form.validate_on_submit():
        username = form.username.data
        response = make_response("")
        response.set_cookie('username', username)
        flash(f"Login Successful as {username.title()}!")      
        next_url = request.args.get('next') or url_for('home')
        response.headers['Location'] = next_url
        response.status_code = 302
        return response
    
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    

