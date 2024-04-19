#!/usr/bin/python3
"""This module contains the definition of the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class representing a State."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    create_engine('mysql://username:password@localhost:3306/database')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='New State')
    session.add(new_state)
    session.commit()


    states = session.query(State).all()
    for state in states:
        print(state.id, state.name)

    session.close()
