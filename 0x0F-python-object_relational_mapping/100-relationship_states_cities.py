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

    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()
