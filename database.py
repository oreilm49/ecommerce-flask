import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import sqlalchemy_jsonfield


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=True)
    catalogs = relationship("Catalog")
    products = relationship("Product")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }


class Global_catalog(Base):
    __tablename__ = 'global'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(String(250), nullable=True)
    tagline = Column(String(250))
    catalogs = relationship("Catalog")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'tagline': self.tagline,
        }


class Catalog(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    image = Column(String(250), nullable=True)
    tagline = Column(String(250))
    global_catalog_id = Column(Integer, ForeignKey('global.id'))
    products = relationship("Product")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'tagline': self.tagline,
            'global_catalog': self.global_catalog_id
        }


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    images = Column(String, nullable=False)
    header = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    price = Column(String(80), nullable=False)
    brand = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    specs = Column(sqlalchemy_jsonfield.JSONField(), nullable=False)
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'images': self.images,
            'header': self.header,
            'model': self.model,
            'price': self.price,
            'brand': self.brand,
            'description': self.description,
            'specs': self.specs,
            'catalog': self.catalog_id
        }


engine = create_engine('postgresql://postgres:access_834@localhost/ecommerce')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
