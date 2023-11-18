#!/usr/bin/python3
"""
script that prints the first State object
from the database hbtn_0e_6_usa
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    str_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(str_db.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
