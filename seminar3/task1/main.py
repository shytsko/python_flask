import random

from flask import Flask, render_template, request, redirect, make_response, url_for, abort
from task1.models import db, Faculty, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    count = 5
    for i in range(1, count + 1):
        new_faculty = Faculty(name=f"Faculty{i}")
        db.session.add(new_faculty)
    # db.session.commit()

    for i in range(1, count ** 2 + 1):
        new_student = Student(
            firstname=f"name{i}",
            lastname=f"lastname{i}",
            age=random.randint(18, 50),
            gender=random.choice(["Женский", "Мужской"]),
            group=i % count + 1,
            faculty_id=i % count + 1,
        )
        db.session.add(new_student)
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)

@app.route('/students/')
def students():
    all_students = Student.query.all()

    context = {
        'title': 'Студенты',
        'students': all_students

    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
