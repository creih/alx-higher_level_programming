#!/usr/bin/python3
"""
this is task 0 mentioned in the README file
"""
import sys
import MySQLdb as msq
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    usrname = sys.argv[1]
    pswd = sys.argv[2]
    dtbs = sys.argv[3]

    dbcon = msq.connect(
        host="localhost",
        port=3306,
        user=usrname,
        passwd=pswd,
        db=dtbs
        )
    cursor = dbcon.cursor()
    qr = "SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC"
    cursor.execute(qr)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    dbcon.close()
