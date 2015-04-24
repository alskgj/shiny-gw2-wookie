__author__ = 'zen'

import sqlalchemy

from DB.sqlalchemy_setup import Price, Item, Base, PATH
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(PATH)

Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()

items = session.query(Item).all()

for item in items:
    print(item.id, item.name)
    price = session.query(Price).filter(Price.item == item).all()[0].price
    print(price)