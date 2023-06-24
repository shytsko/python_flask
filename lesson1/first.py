from flask import Flask, render_template

html_text = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Регистрация</title>
  </head>
  <body>
    <h1>Регистрация</h1>
    <form action="#">
      Ваше имя <input type="text" /><br />
      Пароль <input type="password" /><br />
      Поста <input type="email" /><br />
      Дата рождения <input type="date" /><br />
      <button type="submit">Отправить</button>
      <button type="reset">Сброс</button>
    </form>
  </body>
</html>"""

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return "Hello world!!!"
#
#
# @app.route('/Ваня/')
# def ivan():
#     return "Привет, Ваня!"
#
#
# @app.route('/Коля/')
# def nik():
#     return "Привет, Коля!"
#
#
# @app.route('/Федя/')
# @app.route('/Фёдр/')
# def fed():
#     return "Привет, Федя!"


@app.route('/file/<path:path>/')
def get_file(path):
    return f"Путь к файлу: {path}"


@app.route('/number/<float:num>/')
@app.route('/number/<int:num>/')
def get_number(num):
    return f"Число: {num}"


@app.route('/html/')
def get_html():
    return html_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home/')
def home():
    context = {'title': 'Главная'}
    return render_template('home.html', **context)


@app.route('/contact/')
def contact():
    context = {'title': 'Контакты',
               'email': ['1@1.com', '2@2.com'],
               'tel': ['123344534', '4435245534', '434345634324']}
    return render_template('contact.html', **context)


if __name__ == '__main__':
    app.run()
