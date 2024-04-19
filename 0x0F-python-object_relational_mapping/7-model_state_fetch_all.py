#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """Connect to the MySQL server and list all State objects."""

    engine = create_engine(f'mysql://{username}:{password}\
            @localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state.id, state.name)

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    from model_state import Base, State

    Base.metadata.create_all(create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}'))
    list_states(username, password, database)
