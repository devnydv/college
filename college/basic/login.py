from college import app
from flask import Flask, render_template, request, redirect, url_for, session
from flask import request, jsonify
from college.model import db, admin, Student, Faculty


@app.route("/login/admin", methods = ["GET", "POST"])
def admlogin(): 
    # data = {"username":'admin', "pass":'admin123'}
    # user = admin(username=data['username'], password=data['pass'])
    # db.session.add(user)
    # db.session.commit()
    # return "hmm"
    username = request.form["id"]
    password = request.form["pass"]


    users = admin.query.all()

    user = admin.query.filter_by(username=username).first()
    if user != None:
        if password == user.password and username == user.username:
            session['user_id'] = user.username
        
            return redirect(url_for("admin"))
        else:
            return redirect(url_for("login", message="Invalid credentials"))

    return redirect(url_for("login"))

@app.route("/login/student", methods = ["GET", "POST"])
def student_login():
    
    if request.method == "POST":
        email = request.form["email"]
        phone = request.form["phone"]
        
        user = Student.query.filter_by(email=email).first()
        if user:
            session['student'] = user.id
            print(user.phone) 

            return redirect(url_for("student_profile", id=user.id))
        else:
            return redirect(url_for("login", message="Invalid credentials"))

    return render_template("login.html")

@app.route("/login/faculty", methods = ["GET", "POST"])
def faculty_login():
    if request.method == "POST":
        email = request.form["email"]
        phone = request.form["phone"]

        user = Faculty.query.filter_by(email=email).first()
        if user:
            session['faculty'] = user.id
            return redirect(url_for("faculty_profile", id=user.id))
        else:
            return redirect(url_for("login", message="Invalid credentials"))

    return render_template("login.html")