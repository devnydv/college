from college import app
from college.basic import basic
from college.student import student
from college.admin import admin
from college.faculty import faculty


app.register_blueprint(basic)
app.register_blueprint(student)
app.register_blueprint(admin)
app.register_blueprint(faculty)

if __name__=="__main__":
    app.run(debug=True)