from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/bot")
def diagnostic():
    return render_template("test.html")
@app.route("/login")
def login():
    return render_template("index.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/doctor")
def doctor():
    return render_template("doctor.html")
@app.route("/info")
def info():
    return render_template("info.html")
if __name__=="__main__":
    app.run()
