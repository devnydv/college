from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty
from datetime import datetime

@app.route("/admin/update/student/<id>", methods = ["GET", "POST"])
def updatestdn(id):
    return id