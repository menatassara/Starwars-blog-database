import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    



class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
      
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    user = relationship(User)
    planets = relationship(Planets)
    people = relationship(People)
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')