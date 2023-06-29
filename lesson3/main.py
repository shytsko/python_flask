from flask import Flask, render_template, request, redirect, make_response, url_for, abort, jsonify
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Post, Comment
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


@app.cli.command("edit-john")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')


@app.cli.command("del-john")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')


@app.cli.command("fill-db")
def fill_db():
    count = 5
    for i in range(1, count + 1):
        new_user = User(username=f"user{i}", email=f"user{i}@example.com")
        db.session.add(new_user)
    db.session.commit()

    for i in range(1, count ** 2 + 1):
        new_post = Post(
            title=f"Post {i}",
            content=f"Post {i} text",
            author=User.query.filter_by(username=f"user{i % count + 1}").first()
        )
        db.session.add(new_post)
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная',
        'username': request.cookies.get('username')
    }
    return render_template('index.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        response = make_response(redirect(url_for('hello')))
        response.set_cookie('username', form.username.data)
        return response

    context = {
        'title': 'Авторизация',
        'form': form
    }
    return render_template('login.html', **context)


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('username')
    return response


@app.route('/hello/')
def hello():
    context = {
        'title': 'Привет',
        'username': request.cookies.get('username')
    }
    return render_template('hello.html', **context)


@app.get('/pow2/')
def pow2_get():
    context = {
        'title': 'Привет',
        'username': request.cookies.get('username')
    }
    return render_template('pow2_form.html', **context)


@app.post('/pow2/')
def pow2_post():
    try:
        num = float(request.form.get('number'))
    except ValueError:
        abort(500)

    return redirect(url_for('show_result', number=num, result=num ** 2))


@app.route('/show_result/')
def show_result():
    context = {
        'title': 'Результат',
        'username': request.cookies.get('username'),
        'number': request.args.get('number'),
        'result': request.args.get('result')
    }
    return render_template('show_result.html', **context)


@app.errorhandler(500)
def error500(e):
    context = {
        'title': 'Ошибка сервера',
        'username': request.cookies.get('username'),
    }
    return render_template('500.html', **context)


@app.errorhandler(404)
def error404(e):
    context = {
        'title': 'Ошибка сервера',
        'username': request.cookies.get('username'),
    }
    return render_template('404.html', **context)


@app.route('/users/')
def users():
    all_users = User.query.all()

    context = {
        'title': 'Пользователи',
        'username': request.cookies.get('username'),
        'users': all_users

    }
    return render_template('users.html', **context)


@app.route('/users/<username>')
def users_by_name(username):
    all_users = User.query.filter_by(User.username == username).all()

    context = {
        'title': 'Пользователи',
        'username': request.cookies.get('username'),
        'users': all_users

    }
    return render_template('users.html', **context)


@app.route('/users/<int:user_id>')
def users_by_id(user_id):
    user = User.query.get_or_404(user_id)

    context = {
        'title': 'Пользователи',
        'username': request.cookies.get('username'),
        'users': [user]

    }
    return render_template('users.html', **context)


@app.route('/posts/last-week/')
def get_post_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.author_id == 4).all()

    if posts:
        return jsonify([{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': User.query.get(post.author_id).username,
            'created': post.create_at
        } for post in posts])
    else:
        return jsonify({'error': 'Posts not found'}), 404


if __name__ == '__main__':
    app.run()
