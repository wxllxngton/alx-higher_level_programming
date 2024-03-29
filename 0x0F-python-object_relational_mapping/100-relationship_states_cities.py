#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def setup(username, password, database_name):
    """
    Set up the SQLAlchemy engine, metadata, and session.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): MySQL database name.

    Returns:
        session: SQLAlchemy session object.
    """
    # Create engine and bind it to the session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database_name
        ),
        pool_pre_ping=True,
    )

    # Create the metadata
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    # Call the setup function to create the session
    session = setup(sys.argv[1], sys.argv[2], sys.argv[3])

    # Create State "California" with City "San Francisco"
    try:
        california = State(
            name="California", cities=[City(name="San Francisco")]
        )
        session.add(california)
        session.commit()
    except Exception as err:
        session.rollback()
    finally:
        # Print the new state's ID
        print(california.id)
        session.close()
