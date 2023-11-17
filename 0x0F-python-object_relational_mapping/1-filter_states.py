#!/usr/bin/python3
"""
lists all states with a name starting with N
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    q = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC"
    cur.execute(q)

    rows = cur.fetchall()
    for state in rows:
        print(state)
    cur.close()
    db.close()
