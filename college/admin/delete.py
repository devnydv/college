from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice

@app.route('/admin/faculty/delete/<int:user_id>')
def delete_faculty(user_id):
    user = Faculty.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('faculty'))

@app.route('/admin/student/delete/<int:user_id>')
def delete_student(user_id):
    user = Student.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('stdn'))

@app.route('/admin/notice/delete/<int:user_id>')
def delete_notice(user_id):
    user = Notice.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('notice'))