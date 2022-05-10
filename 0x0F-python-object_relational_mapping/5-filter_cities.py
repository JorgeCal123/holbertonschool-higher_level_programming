#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    """main function"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT states.name, cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    city = []
    for row in query_rows:
        if(row[0] == sys.argv[4]):
            city.append(row[1])
    print(*city, sep=', ')
    cur.close()
