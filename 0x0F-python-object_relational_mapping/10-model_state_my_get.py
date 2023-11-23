#!/usr/bin/python3
"""
Script that prints the State object with the name,
passed as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print(
            "Usage: {} username password database_name state_name".format(
                sys.argv[0]
            )
        )
        exit(1)

    # Create engine and bind it to the session
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Create the metadata
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the provided state name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))

    session.close()
