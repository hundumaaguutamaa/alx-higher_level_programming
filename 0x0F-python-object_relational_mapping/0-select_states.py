#!/usr/bin/python3
"""Script list all states from database hbtn_0e_0_usa"""

import MYSQLdb
from sys import argv

if __name__ == '__main__':

    """   Access to databases and get states from databases. """
    db = MYSQLdb.connect(host="localhost", user=argv[1], port=3306
                         passwd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
