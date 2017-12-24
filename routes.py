from flask import Flask, render_template, request, session, redirect, url_for #import class and function
from models import db, User, Place #import db variable
from forms import SignupFrom, LoginForm, AddressForm
app = Flask(__name__) #creates instance of flask class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oxdhhmjibmrsog:c8ba8f82e10c483d505b7b8335f0bb65551fe87f32135abeaf35d6ac568c30d6@ec2-23-23-245-89.compute-1.amazonaws.com:5432/dcskvq3fhjffd2' #used to attach database to application look at flasksqlalchemy page for more info
db.init_app(app) #initialize app to use this setup

app.secret_key = "development-key" #protects against XSS

@app.route("/") #map this slash to the function index
def index():
    return render_template("index.html") #flask function renders index.html

@app.route("/about") #url for about page
def about():
    return render_template("about.html")

@app.route("/signup", methods=['GET','POST']) # renders signup page
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    form = SignupFrom()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()

            session['email'] = newuser.email #sets email for session object
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('signup.html',form = form)

@app.route("/login", methods=["GET","POST"]) #routing to login page
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    form = LoginForm() #creates form object

    if request.method == "POST":
        if form.validate() == False: #redirects to same page if failed
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data #sets email for session object
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/logout") #pops session which is same as logging out
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route("/home", methods=["GET","POST"]) #private logged in page
def home():
    if 'email' not in session: #checks to see if logged in or not
        return redirect(url_for('login'))

    form = AddressForm()

    places = []
    my_coordinates = (40.1020, 88.2272)

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('home.html', form= form)
        else:
            # get the Address
            address = form.address.data
            # query for places around it
            p = Place()
            my_coordinates = p.address_to_latlng(address)
            places = p.query(address)
            # return those results
            return render_template('home.html', form = form, my_coordinates = my_coordinates, places = places)

    elif request.method == 'GET':
        return render_template("home.html", form = form, my_coordinates = my_coordinates, places = places)

if __name__ == "__main__":
    app.run(debug=True) #turns on debugging for the page
