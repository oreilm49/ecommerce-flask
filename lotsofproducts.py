from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from database import Base, Product, Catalog, User, Global_catalog


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

with open('ecommerce_output.json', 'r') as f:
    products_dict = json.load(f)

session.query(Product).delete()
session.query(Catalog).delete()
session.query(Global_catalog).delete()

# Add global catalogs
for product in products_dict:
    global_catalog_query = session.query(Global_catalog).filter_by(name=product['global_category']).count()
    if global_catalog_query:
        print("global catalog exists")
        continue
    else:
        try:
            session.add(Global_catalog(name=product['global_category']))
            session.commit()
            print("global added: %s") % product['global_category']
        except IOError:
            print(IOError)


# Add catalogs
for product in products_dict:
    catalog_query = session.query(Catalog).filter_by(name=product['category']).count()
    if catalog_query:
        print("catalog exists")
        continue
    else:
        try:
            session.add(Catalog(
                name=product['category'],
                user_id=1,
                global_catalog_id = session.query(Global_catalog).filter_by(name=product['global_category']).one().id
                ))
            session.commit()
            print("catalog added: %s") % product['category']
        except IOError:
            print(IOError)


# Add products
for product in products_dict:
    product_query = session.query(Product).filter_by(model=product['model']).count()
    if product_query:
        print("product exists")
        continue
    else:
        try:
            catalog_id = session.query(Catalog).filter_by(name=product['category']).one().id
            images = ""
            for i in product['images']:
                images += i+","
            session.add(Product(
                    images = images,
                    header = product['header'],
                    model = product['model'],
                    price = product['price'],
                    brand = product['brand'],
                    description = product['description'],
                    specs = product['specs'],
                    catalog_id = catalog_id,
                    user_id=1
                    ))
            session.commit()
            print("Model added %s") % product['model']
        except IOError:
            print(IOError)