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
    str_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(str_db.format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id).filter(State.name.like('%a%')).all()
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
