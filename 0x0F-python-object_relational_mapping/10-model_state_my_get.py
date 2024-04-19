#!/usr/bin/python3
"""
Script to print the State object with the name passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_state_by_name(username, password, database, state_name):
    """Connect to the MySQL server and print the State object with name."""
    engine = create_engine(f'mysql://{username}:{password}\
            @localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> \
                <password> <database> <state_name>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    from model_state import Base, State
    print_state_by_name(username, password, database, state_name)
