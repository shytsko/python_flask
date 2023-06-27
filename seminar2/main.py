from pathlib import PurePath, Path

from flask import Flask, render_template, request, redirect, url_for, abort, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/')
def hello():
    if name := request.args.get('name'):
        text = f"Привет, {name}"
    else:
        text = f"Привет, Мир"
    return text


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    return render_template('upload.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if password == 'password':
            return redirect(url_for('hello', name=name))
        else:
            abort(404)
    return render_template('login.html')


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('number1'))
        num2 = int(request.form.get('number2'))
        operation = request.form.get('operation')

        match operation:
            case 'add':
                result = num1 + num2
            case 'subtract':
                result = num1 - num2
            case 'multiply':
                result = num1 * num2
            case 'divide':
                result = num1 / num2
        return f"{result}"

    return render_template('calc.html')


@app.errorhandler(403)
def error403(error):
    return render_template('403.html')


@app.route('/age/', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            age = int(request.form.get('age'))
            if age < 18:
                raise ValueError()
            return f"Пользователю {name} {age} лет"
        except ValueError:
            abort(403)

    return render_template('age.html')


@app.route('/flash/', methods=['GET', 'POST'])
def flash_():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            flash(f'Привет, {name}!', 'success')
        else:
            flash(f'Нужно ввести имя', 'danger')
        return redirect(url_for('flash_'))
    return render_template('flash.html')


if __name__ == '__main__':
    app.run()
