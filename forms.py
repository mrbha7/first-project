from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length #data required validates imputs in submit

class SignupFrom(Form):
    first_name = StringField('First Name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('Last Name',validators=[DataRequired("Please enter your last name")])
    email = StringField('Email',validators=[DataRequired("Please enter a valid email"), Email("Please enter a valid email")])
    password = PasswordField('Password',validators=[DataRequired("Please enter a password"),Length(min=6, message="Passwords must be atleast 6 characters long")])
    submit = SubmitField('Sign up')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password")])
    submit = SubmitField("Sign in")

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired("Please enter an address.")])
    submit = SubmitField("Search")
