#!/usr/bin/python3
"""
Module that contains the class definition of a City and an instance Base = declarative_base():
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

# Create an instance of declarative_base
Base = declarative_base()


class City(Base):
    """
    City class that represents the 'cities' table in MySQL.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __repr__(self):
        """
        Return a string representation of the City instance.
        """
        return (
            f"<City(id={self.id}, name={self.name}, state_id={self.state_id})>"
        )
