from flask import Flask, render_template
from data import db_session
from data.main_menu import MAIN_MENU

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main_page():
    return render_template('main.html', title='Мята Platinum Белорусская')


@app.route('/menu')
def menu_page():
    return render_template('menu.html')


@app.route('/main_menu')
def main_menu_page():
    db_sess = db_session.create_session()
    pizza = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ПИЦЦА').all()
    snacks = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ЗАКУСКИ').all()
    hot_dishes = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ГОРЯЧИЕ БЛЮДА').all()
    desserts = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ДЕСЕРТЫ').all()
    salads = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'САЛАТЫ').all()
    pasta = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ПАСТА|ВОК|РИЗОТТО').all()
    return render_template('main_menu.html', pizza=pizza, pasta=pasta, hot_dishes=hot_dishes, desserts=desserts,
                           salads=salads, snacks=snacks)


@app.route('/bar_menu')
def bar_menu_page():
    db_sess = db_session.create_session()
    lemon = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ЛИМОНАДЫ').all()
    kofe = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'КОФЕ').all()
    tea = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ЧАИ').all()
    main_kokt = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'АВТОРСКИЕ КОКТЕЙЛИ').all()
    classic_kokt = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'КЛАССИЧЕСКИЕ КОКТЕЙЛИ').all()
    nast = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'НАСТОЙКИ').all()
    return render_template('bar_menu.html', lemon=lemon, kofe=kofe, tea=tea, main_kokt=main_kokt,
                           classic_kokt=classic_kokt, nast=nast)


if __name__ == '__main__':
    db_session.global_init("db/menu.db")
    app.run()
