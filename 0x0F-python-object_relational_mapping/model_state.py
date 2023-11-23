#!/usr/bin/python3
"""
Module that contains the class definition of a State and an instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """
    State class that represents the 'states' table in MySQL.

    Attributes:
        id: Id state
        name: Name of state
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Return a string representation of the State instance.
        """
        return f"<State(id={self.id}, name={self.name})>"
