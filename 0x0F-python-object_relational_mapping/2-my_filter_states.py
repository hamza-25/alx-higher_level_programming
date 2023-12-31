#!/usr/bin/python3
"""
script that takes in an argument and displays all values by user arg
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    cur = db.cursor()

    q = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(q)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
