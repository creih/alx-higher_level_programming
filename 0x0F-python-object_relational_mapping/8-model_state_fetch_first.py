#!/usr/bin/python3
""".alx-token.txt.swp"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    """ Create the engine """
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    print_first_state(username, password, database)
