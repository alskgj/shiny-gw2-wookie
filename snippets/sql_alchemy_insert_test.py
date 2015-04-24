__author__ = 'zen'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from snippets.sql_alchemy_test import Address, Base, Person

engine = create_engine('sqlite:///sqlalch_example.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_person = Person(name='new person')
session.add(new_person)
session.commit()

new_address = Address(post_code='00', person=new_person)
session.add(new_address)
session.commit()