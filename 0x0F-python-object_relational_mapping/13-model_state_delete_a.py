#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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


def delete_states_with_char(session, where_char):
    """
    Deletes all State objects with a name containing the letter 'a' from the database.

    Args:
        session (Session): SQLAlchemy session object.
    """
    try:
        # Delete states with 'a' in their name
        for state in session.query(State):
            if where_char in state.name:
                session.delete(state)
        session.commit()
        print("States deleted successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
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

    # Call the delete_states_with_char function with the created session
    delete_states_with_char(session, where_char="a")
