from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def planet_info(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>
                    <div class="alert alert" role="alert">Претендента на участие в миссии {nickname}:</div>
                    <div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                    <div class="alert alert" role="alert">составляет {rating}!</div>
                    <div class="alert alert-warning" role="alert">Желаем удачи!</div>
                    </h2>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
