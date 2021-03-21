from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/choice/<planet_name>')
def planet_info(planet_name):
    if planet_name.capitalize() == 'Марс':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize()}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета близка к Земле;</div>
                        <div class="alert alert-success" role="alert">На ней много необходимых ресурсов;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть небольшое магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Меркурий':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize()}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета близка к солнцу;</div>
                        <div class="alert alert-success" role="alert">Самая маленькая планета;</div>
                        <div class="alert alert-secondary" role="alert">На ней нет воды и атмосферы;</div>
                        <div class="alert alert-warning" role="alert">Внешне похожа на Луну;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Венера':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize()}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета вторая в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Шестая по размеру планета;</div>
                        <div class="alert alert-secondary" role="alert">На ней нет воды, но есть атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть небольшое магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Земля':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize()}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета третья в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Единственная планета населенная живыми организмами;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Юпитер':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета пятая в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Самая большая планета в Солнечной системе;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Сатурн':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета шестая в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Вторая по размеру планета в Солнечной системе;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть атмосфера, но нет воды;</div>
                        <div class="alert alert-warning" role="alert">На ней есть магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Уран':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Эта планета седьмая в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Третья по размеру планета в Солнечной системе;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''
    elif planet_name.capitalize() == 'Нептун':
        return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name.capitalize}</h1>
                        <h2>
                        <div class="alert alert-dark" role="alert">Последняя планета в Солнечной системе;</div>
                        <div class="alert alert-success" role="alert">Четвертая по размеру планета в Солнечной системе;</div>
                        <div class="alert alert-secondary" role="alert">На ней есть вода и атмосфера;</div>
                        <div class="alert alert-warning" role="alert">На ней есть магнитное поле;</div>
                        <div class="alert alert-danger" role="alert">Наконец она просто красива!</div>
                        </h2>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
