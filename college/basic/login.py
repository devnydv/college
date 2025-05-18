from college import app
from flask import Flask, render_template, request, redirect, url_for, session
from flask import request, jsonify
from college.model import db, admin


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
    user = admin.query.filter_by(username="admin").first()
    if password == user.password and username == user.username:
        session['user_id'] = user.username
        print(session["user_id"])
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("login"))
    