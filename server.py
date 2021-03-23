from flask import Flask, url_for, request
import os


app = Flask(__name__)


@app.route('/')
@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                 <link rel="stylesheet"
                                 href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                 integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                 crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример загрузки файла</title>
                              </head>
                              <body>
                                <h1>Загрузка фотографии</h1>
                                <h2>для участия в миссии</h2>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <img src="static/img/self_image.png" height="400">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        img = open(f'static/img/self_image.png', 'wb')
        img.write(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
