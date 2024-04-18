import sqlalchemy
from .db_session import SqlAlchemyBase
import datetime


class Feetback(SqlAlchemyBase):
    __tablename__ = 'feetback'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now)
