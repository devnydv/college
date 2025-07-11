from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Faculty, Notice

@app.route("/facultyprofile/<id>", methods = ["GET", "POST"])
def faculty_profile(id):
    faculty = Faculty.query.get(id)
    print(faculty)
    if not faculty:
        return "Faculty not found", 404
    return render_template("faculty-profile.html", faculty=faculty, id=id)
