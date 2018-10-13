from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Catalog, Product, Base


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

# CRUD Products
class ProductModel():
    def createProduct(self):
        return "product created"

    def products(self,category):
        return "products"

    def product(self,id):
        return "I'm a product"

    def updateProduct(self,product):
        return "product updated"

    def deleteProduct(self,id):
        return "product deleted"


# CRUD Catalog
class CatalogModel():
    def createCatalog(self):
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
    def createUser(self):
        return "User created"

    def users(self,category):
        return "Users"

    def user(self,id):
        return "User"

    def updateUser(self,product):
        return "User updated"

    def deleteUser(self,id):
        return "User deleted"
