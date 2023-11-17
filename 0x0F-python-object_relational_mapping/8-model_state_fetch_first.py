#!/usr/bin/python3
"""
script that prints the first State object
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    str_db = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(str_db.format(argv[1], argv[2], argv[3]))

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).first()
    if all_states:
        for state in all_states:
            print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
