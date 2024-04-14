#!/usr/bin/python3
"""
this is task 0 mentioned in the README file
"""
import MySQLdb
import sys

def search_states(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    try:
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error: unable to fetch data")
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    cursor.close()
    db.close()
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)
     username = sys.argv[1]
     password = sys.argv[2]
     database = sys.argv[3]
     state_name = sys.argv[4]
     search_states(username, password, database, state_name)
