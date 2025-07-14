from college import app
from flask import Flask, render_template, request, redirect, url_for, session, flash
from college.model import db, Query, Notice
@app.route("/")
def home(): 
    notice = Notice.query.all()
    return render_template("index.html", notices=notice)

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
         if request.method == "POST":
            name = request.form.get("name")
            email = request.form.get("email")
            subject = request.form.get("subject")
            message = request.form.get("message")
            new_query = Query(name=name, email=email, subject=subject, message=message)
            db.session.add(new_query)
            db.session.commit()
            flash("Thank you for your message.")
            return redirect(url_for("contact"))
            
    else:
        return render_template("contact.html")

@app.route("/news")
def news(): 
    return render_template("news.html")

@app.route("/programs")
def programs(): 
    return render_template("programs.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if session.get('user_id'): 
        return redirect(url_for("admin"))
    elif session.get('student'):
        return redirect(url_for("student"))
    elif session.get('faculty'):
        return redirect(url_for("faculty"))
    return render_template("login.html")

