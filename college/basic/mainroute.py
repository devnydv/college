from college import app
from flask import Flask, render_template, request, redirect, url_for, session, flash

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Here you would typically process the form data, e.g., save it to a database or send an email
        flash("Thank you for your message, {}!".format(name))
        print("Contact form submitted")
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

