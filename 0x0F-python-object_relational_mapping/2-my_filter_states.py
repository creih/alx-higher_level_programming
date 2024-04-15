#!/usr/bin/python3
"""
this file is for task nbr 2
"""
import sys
import MySQLdb


def filter_states_by_name(username, password, database, state_name):
    """
    Connect to the MySQL server
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print({}.format(row))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py with 4 args")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    filter_states_by_name(username, password, database, state_name)
