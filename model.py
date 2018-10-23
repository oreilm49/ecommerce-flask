from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database import Catalog, Product, Base, Global_catalog


engine = create_engine('sqlite:///ecommerceapp.db')
Base.metadata.bind = engine


# CRUD Products
class ProductModel():
    def createProduct(self, product):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        print(product)
        catalog = session.query(Catalog).filter_by(id=product['catalog_id']).one()
        newProduct = Product(
                    images = product['images'],
                    header = product['header'],
                    model = product['model'],
                    price = product['price'],
                    brand = product['brand'],
                    description = product['description'],
                    specs = product['specs'],
                    catalog_id = catalog.id)
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
        for p in products:
            p.images = p.images.split(",")
        return products

    def product(self,id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        product = session.query(Product).filter_by(id=id).one()
        product.images = product.images.split(",")
        return product

    def updateProduct(self,product):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        print(product)
        dbproduct = session.query(Product).filter_by(id=product['id']).one()
        if product['model']:
            dbproduct.model = product['model']
        elif product['images']:
            dbproduct.images = product['images']
        elif product['header']:
            dbproduct.header = product['header']
        elif product['price']:
            dbproduct.price = product['price']
        elif product['brand']:
            dbproduct.brand = product['brand']
        elif product['description']:
            dbproduct.description = product['description']
        elif product['specs']:
            dbproduct.specs = product['specs']
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
        global_catalog_id = catalog['global_catalog_id']
        newCatalog = Catalog(
            name=name,
            image=image,
            tagline=tagline,
            global_catalog_id=global_catalog_id
            )
        try:
            session.add(newCatalog)
            session.commit()
            return "New Catalog created"
        except exc.SQLAlchemyError:
            return "Catalog not created"

    def catalogs(self, id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session.query(Catalog).filter_by(global_catalog_id=id).all()

    def allCatalogs(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        return session.query(Catalog)

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
        if catalog['tagline']:
            dbcatalog.tagline = catalog['tagline']
        if catalog['image']:
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

# CRUD Catalog
class GlobalCatalogModel():
    def createGlobal(self, catalog):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        name = catalog['name']
        image = catalog['image']
        tagline = catalog['tagline']
        newCatalog = Global_catalog(
            name=name,
            image=image,
            tagline=tagline)
        try:
            session.add(newCatalog)
            session.commit()
            return "New Global_catalog created"
        except exc.SQLAlchemyError:
            return "Global_catalog not created"

    def global_catalogs(self):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        catalogs = session.query(Global_catalog).all()
        return catalogs

    def global_catalog(self, id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            catalog = session.query(Global_catalog).filter_by(id=id).one()
            return catalog
        except:
            return "Global_catalog with id %s not found" % id

    def updateGlobalCatalog(self, catalog):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        dbcatalog = session.query(Global_catalog).filter_by(id=catalog['id']).one()
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
            return "Global_catalog with id %s updated" % id
        except exc.SQLAlchemyError:
            return "Global_catalog with id %s not updated" % id


    def deleteGlobalCatalog(self, id):
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        try:
            session.query(Global_catalog).filter_by(id=id).delete()
            session.commit()
            return "Global_catalog with id of %s deleted" % id
        except:
            return "SQL Error: Global_catalog with id of %s not deleted"


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


class Workers():
    def getNavLinks(self):
        navlinks = []
        for item in GlobalCatalogModel().global_catalogs():
            output = {}
            output['global'] = item.name
            output['id'] = item.id
            output['catalogs'] = CatalogModel().catalogs(item.id)
            navlinks.append(output)
        return navlinks

    def getSlider(self):
        slider = []
        for item in CatalogModel().allCatalogs():
            if item.image:
                slider.append(item)
        return slider

    def catalogsJSON(self):
        json = []
        for item in GlobalCatalogModel().global_catalogs():
            catalogs = CatalogModel().catalogs(item.id)
            for c in catalogs:
                json.append(c.serialize)
        return json