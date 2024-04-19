#!/usr/bin/python3
"""
task 9 answer or response
"""
import sys
import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_letter_a(username, password, database):
    """ Create the engine for sqlalchemy thingies"""
    engine = create_engine(f'mysql+mysqldb://{username}:\
            {password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('\
            %a%')).order_by(State.id)
    for state in states:
        print(state.id, state.name)
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states_with_letter_a(username, password, database)
