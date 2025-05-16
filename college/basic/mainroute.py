from college import app
from flask import Flask, render_template, request, redirect, url_for, session, flash

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/contact")
def contact(): 
    return render_template("contact.html")

@app.route("/news")
def news(): 
    return render_template("news.html")

@app.route("/programs")
def programs(): 
    return render_template("programs.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    return render_template("login.html")