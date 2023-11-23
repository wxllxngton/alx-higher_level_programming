#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N',
from the hbtn_0e_0_usa database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Creating a cursor
    cur = db.cursor()

    # Execute SQL query to select states with names starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
