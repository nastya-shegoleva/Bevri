from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateField, IntegerField, TimeField, TelField
from wtforms.validators import DataRequired


class ReservForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    phone = TelField('Номер телефона', validators=[DataRequired()])
    date = DateField('Дата', validators=[DataRequired()])
    num_of_guests = IntegerField('Количество гостей', validators=[DataRequired()])
    reserv_time = TimeField('Время брони', validators=[DataRequired()])
    comment = TextAreaField("Комментарий")
    submit = SubmitField('Забронировать')
