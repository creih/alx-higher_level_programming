#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """
    Connect to the MySQL server and delete all
    State objects with a name containing 'a'.
    """
    engine = create_engine(f'mysql://{username}:{password}\
            @localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    from model_state import Base, State

    delete_states_with_a(username, password, database)
