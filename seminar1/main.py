from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/about/')
def about():
    return render_template('about.html', title='Обо мне')


@app.route('/contact/')
def contact():
    return render_template('contact.html', title='Контакты')


@app.route('/sum/<int:num1>/<int:num2>/')
def sum_(num1, num2):
    return str(num1 + num2)


@app.route('/len/<string>/')
def len_(string):
    return str(len(string))


@app.route('/students/')
def students():
    context = {'students':
        [
            {
                'first_name': "Иван",
                'last_name': "Иванов",
                'age': 20,
                'score': 5.0
            },
            {
                'first_name': "Иван",
                'last_name': "Иванов",
                'age': 20,
                'score': 5.0
            },
            {
                'first_name': "Иван",
                'last_name': "Иванов",
                'age': 20,
                'score': 5.0
            }
        ]
    }

    return render_template('students.html', **context)


@app.route('/news/')
def news():
    context = {'news':
        [
            {
                'header': "Новость1",
                'description': "Описание новости1",
                'date': '2023-06-23',
            },
            {
                'header': "Новость2",
                'description': "Описание новости2",
                'date': '2023-06-23',
            },
            {
                'header': "Новость3",
                'description': "Описание новости3",
                'date': '2023-06-23',
            }
        ]
    }

    return render_template('news.html', **context)


if __name__ == '__main__':
    app.run()
