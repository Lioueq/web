from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/distribution')
def distribution():
    crew = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бич']
    return render_template('distribution.html', crew=crew)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
