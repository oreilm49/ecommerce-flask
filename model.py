from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database import Catalog, Product, Base


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

# CRUD Products
class ProductModel():
    def createProduct(self, product):
        name = product['name']
        price = product['price']
        image = product['image']
        description = product['description']
        category = session.query(Catalog).filter_by(name=product['category'])
        newProduct = Product(name=name,price=price,image=image,description=description,catalog=category)
        try:
            session.add(newProduct)
            session.commit()
            return "New product created"
        except exc.SQLAlchemyError:
            return "Product not created"

    def products(self,category):
        catalog = session.query(Catalog).filter_by(name=category)
        products = session.query(Product).filter_by(catalog_id=catalog.id)
        session.commit()
        return products

    def product(self,id):
        product = session.query(Product).filter_by(id=id).one()
        session.commit()
        return product

    def updateProduct(self,product):
        id = product['id']
        name = product['name']
        price = product['price']
        image = product['image']
        description = product['description']
        category = session.query(Catalog).filter_by(name=product['category'])
        editedProduct = Product(name=name,price=price,image=image,description=description,catalog=category)
        try:
            session.add(editedProduct)
            session.commit()
            return "Product created"
        except exc.SQLAlchemyError:
            return "Product not created"

    def deleteProduct(self,id):
        try:
            session.query(Product).filter_by(id=id).delete()
            session.commit()
            return "Product with id of %s deleted" % id
        except:
            return "SQL Error: product not deleted"

# CRUD Catalog
class CatalogModel():
    def createCatalog(self, catalog):
        return "Catalog created"

    def catalogs(self):
        return session.query(Catalog).all()

    def catalog(self, id):
        return "Catalog"

    def updateCatalog(self, product):
        return "Catalog updated"

    def deleteCatalog(self, id):
        return "Catalog deleted"


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
