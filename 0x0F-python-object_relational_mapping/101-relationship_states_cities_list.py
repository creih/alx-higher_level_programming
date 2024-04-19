#!/usr/bin/python3
"""
Script to list all State objects and correspondin
g City objects contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

def list_states_and_cities(username, password, database):
    """
    Connect to the MySQL server and list all
    State objects and corresponding City objects.
    """
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    from relationship_state import Base, State
    list_states_and_cities(username, password, database)
