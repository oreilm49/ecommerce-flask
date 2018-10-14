from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database import Catalog, Product, Base


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.bind = engine


# CRUD Products
class ProductModel():
    def createProduct(self, product):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        name = product['name']
        price = product['price']
        image = product['image']
        description = product['description']
        catalog = session.query(Catalog).filter_by(id=product['catalog_id']).one()
        newProduct = Product(
            name=name,
            price=price,
            image=image,
            description=description,
            catalog=catalog)
        try:
            session.add(newProduct)
            session.commit()
            return "New product created"
        except exc.SQLAlchemyError:
            return "Product not created"

    def products(self,category):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        products = session.query(Product).filter_by(catalog_id=category).all()
        return products

    def product(self,id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        product = session.query(Product).filter_by(id=id).one()
        session.commit()
        return product

    def updateProduct(self,product):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        dbproduct = session.query(Product).filter_by(id=product['id']).one()
        if product['name']:
            dbproduct.name = product['name']
        elif product['price']:
            dbproduct.price = product['price']
        elif product['image']:
            dbproduct.image = product['image']
        elif product['description']:
            dbproduct.description = product['description']
        try:
            session.add(dbproduct)
            session.commit()
            return "Product with id %s updated" % id
        except exc.SQLAlchemyError:
            return "Product with id %s not updated" % id

    def deleteProduct(self,id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            session.query(Product).filter_by(id=id).delete()
            session.commit()
            return "Product with id of %s deleted" % id
        except:
            return "SQL Error: roduct with id of %s not deleted"

# CRUD Catalog
class CatalogModel():
    def createCatalog(self, catalog):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        name = catalog['name']
        image = catalog['image']
        tagline = catalog['tagline']
        newCatalog = Catalog(
            name=name,
            image=image,
            tagline=tagline)
        try:
            session.add(newCatalog)
            session.commit()
            return "New Catalog created"
        except exc.SQLAlchemyError:
            return "Catalog not created"

    def catalogs(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        catalogs = session.query(Catalog).all()
        session.commit()
        return catalogs

    def catalog(self, id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            catalog = session.query(Catalog).filter_by(id=id).one()
            return catalog
        except:
            return "Catalog with id %s not found" % id

    def updateCatalog(self, catalog):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        dbcatalog = session.query(Catalog).filter_by(id=catalog['id']).one()
        if catalog['name']:
            dbcatalog.name = catalog['name']
        elif catalog['tagline']:
            dbcatalog.tagline = catalog['tagline']
        elif catalog['image']:
            dbcatalog.image = catalog['image']
        else:
            pass
        try:
            session.add(dbcatalog)
            session.commit()
            return "Catalog with id %s updated" % id
        except exc.SQLAlchemyError:
            return "Catalog with id %s not updated" % id


    def deleteCatalog(self, id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            session.query(Catalog).filter_by(id=id).delete()
            session.commit()
            return "Catalog with id of %s deleted" % id
        except:
            return "SQL Error: catalog with id of %s not deleted"


# CRUD User
class UserModel():
    def createUser(self, user):
        return "User created"

    def users(self,category):
        return "Users"

    def user(self,id):
        return "User"

    def updateUser(self,product):
        return "User updated"

    def deleteUser(self,id):
        return "User deleted"
