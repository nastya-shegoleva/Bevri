from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, FormField, IntegerField
from wtforms.validators import DataRequired


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[DataRequired()])
    area_code = IntegerField('Area Code/Exchange', validators=[DataRequired()])
    number = StringField('Number')


class ReservForm(FlaskForm):
    name = StringField('Имя пользователя', validators=[DataRequired()])
    phone = FormField(TelephoneForm)
    date = DateTimeField('Дата', validators=[DataRequired()])
    num_of_guests = IntegerField('Количество гостей', validators=[DataRequired()])
    reserv_time = DateTimeField('Время брони', validators=[DataRequired()])
    comment = TextAreaField("Комментарий")
    submit = SubmitField('Забронировать')
