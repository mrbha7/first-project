from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Email, Length #data required validates imputs in submit

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
  address = StringField('Location', validators=[DataRequired("Please enter a valid address or location")])
  submit = SubmitField("Search")

class BudgetForm(Form):
    budget = FloatField('Budget', validators =[InputRequired("Please enter a Budget")]) #work needed here
    days = IntegerField('Days', validators =[InputRequired("Please enter number of days on trip")])
    nights = IntegerField('Nights', validators =[InputRequired("Please enter number of nights on trip")])
    hotel = FloatField('Hotel Cost Per Night', validators =[InputRequired("Please enter a Per Night cost of a Hotel")])
    cRental = FloatField('Car Rental Per Day', validators =[InputRequired("Please enter a per day Rental Price, enter 0 if N/A")])
    submit = SubmitField("Calculate")
