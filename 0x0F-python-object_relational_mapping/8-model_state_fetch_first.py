#!/usr/bin/python3
"""
Script to print the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_first_state(username, password, database):
    """Connect to the MySQL server and print the first State object."""

    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(first_state.id, first_state.name)
    else:
        print("No records found in the database.")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    from model_state import Base, State

    print_first_state(username, password, database)
