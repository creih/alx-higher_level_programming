#!/usr/bin/python3
"""
this is a file for task nbr 2
"""
import sys
import MySQLdb

def filter_states_by_name(username, password, database, state_name):
    """
    Connect to the MySQL server
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve states matching the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    filter_states_by_name(username, password, database, state_name)
