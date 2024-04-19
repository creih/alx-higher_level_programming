#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def create_california_with_san_francisco(username, password, database):
    """
    Connect to the MySQL server and create the State 
    "California" with the City "San Francisco".
    """
      engine = create_engine(f'mysql://{username}:{password}@\
              localhost:3306/{database}')

    Session = sessionmaker(bind=engine)
    session = Session()

    california = State(name='California', cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    from relationship_state import Base, State
    from relationship_city import City

    create_california_with_san_francisco(username, password, database)
