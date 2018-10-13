from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from database import Base, Product, Catalog, User


engine = create_engine('sqlite:///ecommerceapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

with open('products.json', 'r') as f:
    products_dict = json.load(f)

for product in products_dict:
    if all (p in product for p in ('model','price','image')):
        productQuery = session.query(Product).filter_by(name=product['model']).count()
        catalogQuery = session.query(Catalog).filter_by(name=product['category']).count()
        session.commit()
        if catalogQuery:
            if productQuery:
                print("Product already exists")
            else:
                catalog = session.query(Catalog).filter_by(name=product['category']).one()
                newProduct = Product(
                    name=product['model'],
                    description="please update description",
                    price=product['price'],
                    catalog=catalog,
                    image=product['image'])
                session.add(newProduct)
                session.commit()
        else:
            newCatalog = Catalog(name=product['category'],image='',tagline='')
            session.add(newCatalog)
            session.commit()
            newProduct = Product(
                    name=product['model'],
                    description="please update description",
                    price=product['price'],
                    catalog=newCatalog,
                    image=product['image'])
            session.add(newProduct)
            session.commit()