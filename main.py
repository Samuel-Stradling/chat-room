from flask import Flask, render_template

app = Flask(__name__)

# when the directory is '/' , the function returns the html following
@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"


# when a user visits the home directory with /login , flask goes to the templates folder and renders loginpage.html
@app.route("/login/")
def login(name=None):
    return render_template("loginpage.html", name=name)
