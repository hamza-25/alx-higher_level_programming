#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                argv[2],
                argv[3])
            )

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id.asc()).all()
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
