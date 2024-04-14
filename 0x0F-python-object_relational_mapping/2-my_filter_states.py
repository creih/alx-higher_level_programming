#!/usr/bin/python3
"""
this is task 0 mentioned in the README file
"""
import sys
import MySQLdb as msq
if len(sys.argv) != 5:
    print("Usage: python script.py <username> <password> <database>")
    sys.exit(1)
usrname = sys.argv[1]
pswd = sys.argv[2]
dtbs = sys.argv[3]
data = sys.argv[4]

dbcon = msq.connect(
        host="localhost",
        port=3306,
        user=usrname,
        passwd=pswd,
        db=dtbs
        )
cursor = dbcon.cursor()
qr = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
cursor.execute(qr, (data,))
states = cursor.fetchall()
for state in states:
    print(state)
cursor.close()
dbcon.close()
