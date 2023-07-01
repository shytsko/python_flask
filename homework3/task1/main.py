# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from flask import Flask, render_template, request, redirect, make_response, url_for, abort
from .models import db, Faculty, Student, Grade, Discipline, Performance
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    count = 3
    for i in range(1, count + 1):
        new_faculty = Faculty(name=f"Faculty{i}")
        db.session.add(new_faculty)

    students_ = [Student(
        firstname=f"name{i}",
        lastname=f"lastname{i}",
        age=random.randint(18, 50),
        gender=random.choice(["Женский", "Мужской"]),
        group=i % count + 1,
        email=f"name{i}@mail.com",
        faculty_id=i % count + 1)
        for i in range(1, count ** 2 + 1)]

    db.session.add_all(students_)

    grades = [Grade(value=2, alias='неудовлетворительно'),
              Grade(value=3, alias='удовлетворительно'),
              Grade(value=4, alias='хорошо'),
              Grade(value=5, alias='отлично')]
    db.session.add_all(grades)

    disciplines = [Discipline(name='Базы данных'),
                   Discipline(name='Алгоритмы и структуры данных'),
                   Discipline(name='Веб-технологии'),
                   Discipline(name='Математика'),
                   Discipline(name='Объектно-ориентированное программирование')]
    db.session.add_all(disciplines)

    for _ in range(count ** 4):
        db.session.add(
            Performance(student=random.choice(students_),
                        discipline=random.choice(disciplines),
                        grade=random.choice(grades)))

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


@app.route('/grades/')
def grades():
    all_students = Student.query.all()
    context = {
        'title': 'Оценки',
        'students': all_students
    }
    return render_template('grades.html', **context)


if __name__ == '__main__':
    app.run()
