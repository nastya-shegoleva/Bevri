from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main_page():
    return render_template('main.html', title='Мята Platinum Белорусская')


@app.route('/menu')
def menu_page():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run()
