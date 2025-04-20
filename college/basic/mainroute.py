from college import app
from flask import Flask, render_template, request, redirect, url_for, session, flash

@app.route("/")
def home():
    
    return render_template("base.html")