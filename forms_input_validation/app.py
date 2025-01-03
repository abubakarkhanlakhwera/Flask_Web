from flask import Flask , render_template,redirect,url_for,flash
from forms import SignupForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup',methods=['POST','GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        flash(f'Login successful for {form.email.data}!','success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
    