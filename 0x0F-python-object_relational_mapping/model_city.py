#!/usr/bin/python3
"""
Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Representation of class City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
