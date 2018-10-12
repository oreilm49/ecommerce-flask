import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    image = Column(String(250), nullable = False)
    tagline = Column(String(250))
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'tagline': self.tagline,
        }


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    price = Column(String(80), nullable = False)
    image = Column(String(250), nullable = False)
    description = Column(String(250), nullable = False)
    catalog = relationship(Catalog)
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'image': self.image,
            'description': self.description,
            'catalog': self.catalog,
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind = engine)
