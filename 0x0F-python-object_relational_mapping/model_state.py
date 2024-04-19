#!/usr/bin/python3
"""
task model_state is about joining sql alchemy in our python codes
"""
import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    state class meant to define how the id should be
    """
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True
            )
    name = Column(
            String(128),
            nullable=False
            )
