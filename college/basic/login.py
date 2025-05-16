from college import app
from flask import Flask, render_template, request, redirect
from flask import request, jsonify
from college.model import db, admin


@app.route("/login/admin", methods = ["GET", "POST"])
def admlogin(): 
    # data = {"username":'admin', "pass":'admin123'}
    # user = admin(username=data['username'], password=data['pass'])
    # db.session.add(user)
    # db.session.commit()
    # return "hmm"
    users = admin.query.all()
    return jsonify([user.to_dict() for user in users])
    data =  request.form
    print(data)
    return render_template("index.html")