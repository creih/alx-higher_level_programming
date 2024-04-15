#!/usr/bin/python3
"""
task model_state is about joining sql alchemy in our python codes
"""
import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base as Base


class State(Base):
    """
    state class meant to define how the id should be
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


eng = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

Base.metadata.create_all(eng)
