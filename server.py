from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def text():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми'\
           'безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!'


@app.route('/image_mars')
def img():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <h1>Привет, Марс!</h1>
                  </head>
                  <body>
                    <img src="static/img/MARS.png" alt="Фото Марса">
                  <div>Жди нас, Марс!</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
