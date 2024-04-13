#!/usr/bin/python3
"""
this is task 0 mentioned in the README file
"""
import sys
import MySQLdb as msq
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
qr = "SELECT id, states FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cursor.execute(qr)
states = cursor.fetchall()
for state in states:
    print(state)
