from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField,SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, Optional,EqualTo

class SignupForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=4, max=30)]
                           )
    email = StringField("Email",
                        validators=[DataRequired(), Email()]
                        )
    gender = SelectField(
        "Gender",
        choices = ["Male","Female","Other"],
        validators=[Optional()]
    )
    dob = DateField("Date of Birth", format='%Y-%m-%d', validators=[Optional()])
    
    password = PasswordField("Password",
                                validators=[DataRequired(), Length(min=4, max=80)]
                                )
    confirm_password = PasswordField("Confirm Password",
                                validators=[DataRequired(), Length(min=4, max=80),EqualTo('password')]
                                )
    submit = SubmitField("Sign Up")
    
class LoginForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired()]
                           )
    password = PasswordField("Password",
                                validators=[DataRequired(), Length(min=4, max=80)]
                                )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")