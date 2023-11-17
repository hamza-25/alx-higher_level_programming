#!/usr/bin/python3
"""
script that takes in an argument and displays all values by user arg
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    q = "SELECT * FROM states WHERE name = '{}' \
    ORDER BY states.id ASC".format(argv[4])
    cur.execute(q)

    state = cur.fetchone()
    print(state)
    cur.close()
    db.close()
