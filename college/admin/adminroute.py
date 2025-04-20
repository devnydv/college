from college import app
from flask import render_template, request, redirect, session, url_for



@app.route("/admin/student", methods = ["GET", "POST"])
def admin():
    #inser = addtablerow()
    
    return render_template("student.html")
    