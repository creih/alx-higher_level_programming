#!/usr/bin/python3
"""
task model_state
"""
import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """state class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')

Base.metadata.create_all(engine)
