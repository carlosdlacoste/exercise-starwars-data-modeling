import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    user_name = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    subscription_date = Column(Date(), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    descripcion = Column(String(150), nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    descripcion = Column(String(150), nullable=False)

class Favorito(Base):
    __tablename__ = 'favorito'
    
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    personaje = relationship(Personaje)
    planeta = relationship(Planeta)
    usuario = relationship(Usuario)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
#     usuario = relationship(Usuario)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
