#!/usr/bin/python3
"""
task 4 file
"""
import sys
import MySQLdb


def list_cities(username, password, database):
    """list of cities from task 4"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name,states.name FROM cities \
            JOIN states ON cities.state_id = states.id  ORDER BY cities.id ASC"
    cursor.execute(query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, database)
