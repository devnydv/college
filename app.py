from college import app
from college.basic import basic
from college.student import student
from college.admin import admin

app.register_blueprint(basic)
app.register_blueprint(student)
app.register_blueprint(admin)

if __name__=="__main__":
    app.run(debug=True)