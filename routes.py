from flask import Flask, render_template #import class and function
from models import db #import db variable
app = Flask(__name__) #creates instance of flask class

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask' #used to attach database to application look at flasksqlalchemy page for more info
db.init_app(app) #initialize app to use this setup

@app.route("/") #map this slash to the function index
def index():
    return render_template("index.html") #flask function renders index.html
@app.route("/about") #url for about page
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) #turns on debugging for the page
