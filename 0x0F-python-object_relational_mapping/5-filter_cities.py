#!/usr/bin/python3
"""
task 5 about displaying city be state
"""
import sys
import MySQLdb


def list_cities_by_state(
        username,
        password,
        database,
        state_name
        ):
    """Connect to the MySQL server and display cities"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(', '.join(row[0] for row in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py with 4 args")
        sys.exit(1)

    username = sys.argv[1],
    password = sys.argv[2],
    database = sys.argv[3],
    state_name = sys.argv[4]
    list_cities_by_state(username, password, database, state_name)
