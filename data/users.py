import sqlalchemy
from sqlalchemy_utils import PhoneNumberType
from .db_session import SqlAlchemyBase


class USERS(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phone_number = sqlalchemy.Column(PhoneNumberType(), unique=True)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    num_of_guests = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    reserv_time = sqlalchemy.Column(sqlalchemy.Time, nullable=True)
    comment = sqlalchemy.Column(sqlalchemy.TEXT)
