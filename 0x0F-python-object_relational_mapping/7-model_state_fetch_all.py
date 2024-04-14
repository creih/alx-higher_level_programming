#!/usr/bin/python3
"""
task 7 response is all in this file
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(username, password, database):
    """Create the engine"""
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
