from flask import Flask, render_template
import json
from random import choice


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/member')
def member():
    with open('templates/crew.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        member = choice(data['member'])
    return render_template('member.html', **member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
