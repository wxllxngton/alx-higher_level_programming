#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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


def add_state(session, new_state_name):
    """
    Add a new state to the database and print its ID.

    Args:
        session (Session): SQLAlchemy session object.
        new_state_name (str): Name of the new state.
    """
    try:
        # Add new state
        new_state = State(name=new_state_name)
        session.add(new_state)
        session.commit()

        # Print the new state's ID
        print(
            "{}".format(
                session.query(State)
                .filter(State.name == new_state_name)
                .first()
                .id
            )
        )
    finally:
        # Close the session
        session.close()


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    # Call the setup function to create the session
    session = setup(sys.argv[1], sys.argv[2], sys.argv[3])

    # Call the add_state function with the created session
    add_state(session, new_state_name="Louisiana")
