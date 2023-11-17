#!/usr/bin/python3
"""List all state order by id"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    host = 'localhost'
    db = MySQLdb.connect(host=host, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name LIKE 'N%'ORDER BY states.id ASC"
    cur.execute(q)
    rows = cur.fetchall()
    for state in rows:
        print(state)
    db.commit()
    cur.close()
    db.close()
