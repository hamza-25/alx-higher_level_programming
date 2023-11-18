#!/usr/bin/python3
"""
python file that contains the class definition
of a State and an instance
"""


from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from model_city import City

Base = declarative_base()


class State(Base):
    """Representation of class state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(length=128), unique=True)
    cities = relationship('City', backref='states')
