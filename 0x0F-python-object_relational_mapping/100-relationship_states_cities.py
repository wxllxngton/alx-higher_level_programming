#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa.
"""

if __name__ == "__main__":
    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    # # Create State "California" with City "San Francisco"
    # california = State(name="California", cities=[City(name="San Francisco")])
    # session.add(california)
    # session.commit()

    # # Print the new state's ID
    # print(california.id)

    new_city = City(name="San Francisco")
    new_states = State(name="California")
    new.cities.append(new_city)
    session.add_all([new_states, new_city])
    session.commit()
    session.close()
