from flask import Flask, render_template, redirect
from data import db_session
from data.main_menu import MAIN_MENU
from data.users import USERS
from forms.reserv import ReservForm, TelephoneForm

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
    game_wine = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ИГРИСТЫЕ ВИНА').all()
    white_wine = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'БЕЛЫЕ ВИНА').all()
    red_wine = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'КРАСНЫЕ ВИНА').all()
    vermouth = db_sess.query(MAIN_MENU).filter(MAIN_MENU.type == 'ВЕРМУТЫ').all()
    return render_template('bar_menu.html', lemon=lemon, kofe=kofe, tea=tea, main_kokt=main_kokt,
                           classic_kokt=classic_kokt, nast=nast, game_wine=game_wine, white_wine=white_wine,
                           red_wine=red_wine,
                           vermouth=vermouth)


'''@app.route('/reserving')
def reserv():
    return render_template('reserv.html')
'''


@app.route('/reserving', methods=['GET', 'POST'])
def reserv():
    form1, form2 = ReservForm(), TelephoneForm
    if form1.validate_on_submit() and form1.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(USERS).filter(USERS.name == form1.name.data).first():
            return render_template('reserv.html', title='Бронирование',
                                   form=form1,
                                   message="Вы уже регистрировали столик")
        user = USERS(
            name=form1.name.data,
            phone_country_code=form2.country_code.data,
            _phone_number=form2.number,
            phone=form1.phone,
            date=form1.date.data,
            num_of_guests=form1.num_of_guests.data,
            reserv_time=form1.reserv_time.data,
            comment=form1.comment
            )
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('reserv.html', title='Бронирование', form=form1)


if __name__ == '__main__':
    db_session.global_init("db/menu.db")
    app.run()
