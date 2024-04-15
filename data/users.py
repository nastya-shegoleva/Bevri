import sqlalchemy
from sqlalchemy_utils import PhoneNumber
from .db_session import SqlAlchemyBase


class USERS(SqlAlchemyBase):
    __tablename__ = 'Пользователи'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    _phone_number = sqlalchemy.Column(sqlalchemy.Unicode(255))
    phone_country_code = sqlalchemy.Column(sqlalchemy.Unicode(8))

    phone_number = sqlalchemy.orm.composite(
        PhoneNumber,
        _phone_number,
        phone_country_code)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    num_of_guests = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    reserv_time = sqlalchemy.Column(sqlalchemy.Time, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.TEXT)
