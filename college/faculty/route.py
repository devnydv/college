from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Faculty, Notice
from sqlalchemy import desc
@app.route("/facultyprofile/<id>", methods = ["GET", "POST"])
def faculty_profile(id):
    if session.get('faculty') is None:
        return redirect(url_for("login"))
    else:
        faculty = Faculty.query.get(id)
        notices = Notice.query.order_by(desc(Notice.id)).limit(3).all()
        if not faculty:
            return "Faculty not found", 404
        return render_template("faculty-profile.html", faculty=faculty, id=id, logged_in=True, notices=notices)
