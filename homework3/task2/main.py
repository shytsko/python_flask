# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля
# "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
#
# Доделать задачу 4: добавить проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.
#
# Дополнительно из задачи 5: добавить подтверждение пароля, дату рождения, согласие на обработку персональных данных.
# При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации

# Дополнительно из задачи 7:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.

from flask import Flask, render_template, request, redirect, make_response, url_for, abort
from .models import db, User
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task2_data.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    first_user = User(
        nickname="vasya",
        firstname="Вася",
        lastname="Пупкин",
        email="pupkin@mail.com",
        birth_date=datetime(2000, 1, 1, 0, 0, 0),
        psw_hash=generate_password_hash('abc123456')
    )
    db.session.add(first_user)
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)


@app.route('/register/')
def register():
    context = {
        'title': 'Регистрация',
    }
    return render_template('register.html', **context)


if __name__ == '__main__':
    app.run()
