#!/usr/bin/python3
"""
task 5 about displaying city be state
"""
import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
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
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    list_cities_by_state(username, password, database, state_name)
