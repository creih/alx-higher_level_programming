#!/usr/bin/python3
"""
Script to change the name of a State object in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database):
    """Connect MySQL server and change the name of a State object."""

    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    from model_state import Base, State

    change_state_name(username, password, database)
