#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa,
where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print(
            "Usage: {} username password database_name state_name".format(
                argv[0]
            )
        )
        exit(1)

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Creating a cursor
    cur = db.cursor()

    # Select states with the given name using a parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
