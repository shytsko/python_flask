# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template
import database

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/home/')
def index():
    context = {
        'title': 'Главная',
        'categories': database.get_categories()
    }
    return render_template('index.html', **context)


@app.route('/categories/<category>/')
def сategories(category):
    context = {
        'title': category
    }
    return render_template('сategories.html', **context)


if __name__ == '__main__':
    app.run()
