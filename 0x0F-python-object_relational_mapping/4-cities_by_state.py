#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    # Creating a cursor
    cur = db.cursor()

    # Execute SQL query to select cities with the corresponding state names
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
