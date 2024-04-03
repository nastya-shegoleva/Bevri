import sqlalchemy
from .db_session import SqlAlchemyBase


class MAIN_MENU(SqlAlchemyBase):
    __tablename__ = 'ГЛАВНОЕ МЕНЮ'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    weight = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True, index=True)
