from flask_sqlalchemy import SQLAlchemy #uses extention in this file
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy() #creates database variable

class User(db.Model): #creates python class to model columns in the table
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique = True)
    pwdhash = db.Column(db.String(54))

    def __init__(self,firstname,lastname,email,password): # constructor to set attributes
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self,password): #function to encrypt password
        self.pwdhash = generate_password_hash(password)

    def check_password(self,password): # used to check password
        return check_password_hash(self.pwdhash, password)
