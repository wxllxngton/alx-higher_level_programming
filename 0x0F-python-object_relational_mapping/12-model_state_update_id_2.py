#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
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


def update_state(session, where_id, new_state_name):
    """
    Updates the name of a State object in the database.

    Args:
        session (Session): SQLAlchemy session object.
        where_id (int): ID of the state to be updated.
        new_state_name (str): New name for the state.
    """
    try:
        # Update state
        state = session.query(State).filter(State.id == where_id).first()

        if state:
            state.name = new_state_name
            session.commit()
            print("State name updated successfully!")
        else:
            print("State not found.")

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

    # Call the update_state function with the created session
    update_state(session, where_id=2, new_state_name="New Mexico")
