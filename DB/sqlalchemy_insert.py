__author__ = 'zen'

from DB.sqlalchemy_setup import Price, Item, Base, PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

NOW = int(time.time())

def _get_session():
    engine = create_engine(PATH)
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session


def insert(name, price, offers, timestamp=NOW):
    session = _get_session()

    # add item iff it isn't in the db yet.
    if not session.query(Item).filter(Item.name == name).count():
        new_item = Item(name=name)
        session.add(new_item)

    new_price = Price(price=price, timestamp=timestamp, offers=offers, item_name=name)
    session.add(new_price)

    session.commit()
