__author__ = 'zen'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy
from os import path

PATH = 'sqlite:///'+path.dirname(__file__)+"\\main.db"


Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(250), nullable=False, unique=True)


class Price(Base):
    __tablename__ = 'price'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    timestamp = sqlalchemy.Column(sqlalchemy.Integer)
    offers = sqlalchemy.Column(sqlalchemy.Integer)

    item_name = sqlalchemy.Column(sqlalchemy.String(250), sqlalchemy.ForeignKey('item.name'))
    item = relationship(Item)

engine = sqlalchemy.create_engine(PATH)

Base.metadata.create_all(engine)