#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
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

    # Execute SQL query to select cities with the corresponding state names
    query = """
        SELECT cities.name
        FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    state_name = argv[4]
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Check if any cities were found
    if not rows:
        print("No cities found for the state {}".format(state_name))
    else:
        # Print the rows
        cities = [row[0] for row in rows]
        print(", ".join(cities))

    # Close cursor and database connection
    cur.close()
    db.close()
