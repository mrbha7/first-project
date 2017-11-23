from flask import Flask, render_template #import class and function

app = Flask(__name__) #creates instance of flask class

@app.route("/") #map this slash to the function index
def index():
    return render_template("index.html") #flask function renders index.html
@app.route("/about") #url for about page
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) #turns on debugging for the page
