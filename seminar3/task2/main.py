import random

from flask import Flask, render_template, request, redirect, make_response, url_for, abort
from task2.models import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.drop_all()
    db.create_all()
    print('OK')


@app.cli.command("fill-db")
def fill_db():
    author1 = Author(firstname='Author1', lastname='Author1_last')
    author2 = Author(firstname='Author2', lastname='Author2_last')
    author3 = Author(firstname='Author3', lastname='Author3_last')

    book1 = Book(title='Book1', year=2022, count=1000)
    book2 = Book(title='Book2', year=2020, count=2000)
    book3 = Book(title='Book3', year=2000, count=3000)
    book4 = Book(title='Book4', year=2021, count=4000)
    book5 = Book(title='Book5', year=2023, count=5000)

    book1.authors.append(author1)
    book2.authors.append(author2)
    book2.authors.append(author3)
    book3.authors.append(author1)
    book4.authors.append(author2)
    book4.authors.append(author1)
    book5.authors.append(author3)

    db.session.add_all([author1, author2, author3, book1, book2, book3, book4, book5])
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная',
    }
    return render_template('index.html', **context)


@app.route('/books/')
def books():
    all_books = Book.query.all()

    context = {
        'title': 'Книги',
        'books': all_books
    }
    return render_template('books.html', **context)


@app.route('/authors/')
def authors():
    authors = Author.query.all()

    context = {
        'title': 'Авторы',
        'authors': authors
    }
    return render_template('authors.html', **context)


if __name__ == '__main__':
    app.run()
