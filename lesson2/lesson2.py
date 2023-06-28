from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/<path:user_text>/')
def text(user_text):
    return escape(user_text)


@app.route('/escape/<path:user_text>')
def escape_ex(user_text):
    return render_template('escape.html', text=user_text)


if __name__ == '__main__':
    app.run()
