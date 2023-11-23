#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
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

    # Query and print all State and City objects
    states_and_cities = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(State.id, City.id)
        .all()
    )

    current_state_id = None

    for state, city in states_and_cities:
        if state.id != current_state_id:
            print("{}: {}".format(state.id, state.name))
            current_state_id = state.id
        print("    {}: {}".format(city.id, city.name))
