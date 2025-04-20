from college import app
from flask import render_template, request, redirect, session, url_for


@app.route("/student", methods = ["GET", "POST"])
def table():
    #inser = addtablerow()
    return render_template("profile.html")
    