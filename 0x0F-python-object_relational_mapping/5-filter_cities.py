#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
    state = argv[4]
    cur.execute("SELECT cities.name FROM cities \
            WHERE state_id = \
            (SELECT id FROM states WHERE name LIKE BINARY %s)", (state, ))
    cities = cur.fetchall()
    names = [city[0] for city in cities]
    print(', '.join(names))
    cur.close()
    db.close()
