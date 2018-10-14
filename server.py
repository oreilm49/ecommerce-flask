from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from model import ProductModel, CatalogModel, UserModel
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from database import Catalog, Product, Base


app = Flask(__name__)

# Defined once, used in each client template for nav links
catalogs = CatalogModel().catalogs()

# Home route
@app.route('/')
def index():
    products = ProductModel().products(1)
    return render_template('index.html',catalogs=catalogs,products=products)

# Category page
@app.route('/catalog/<int:catalog_id>/products')
def categoryCatalog(catalog_id):
    products = ProductModel().products(catalog_id)
    catalog = CatalogModel().catalog(catalog_id)
    return render_template('category.html',catalogs=catalogs,catalog=catalog,products=products)

# Product page
@app.route('/catalog/<int:catalog_id>/product/<int:id>')
def productPage(catalog_id, id):
    product = ProductModel().product(id)
    catalog = CatalogModel().catalog(catalog_id)
    return render_template('product.html',catalogs=catalogs,product=product,catalog=catalog)

# Products JSON
@app.route('/catalog/<int:catalog_id>/products/JSON')
def categoryCatalogJSON(catalog_id):
    products = ProductModel().products(catalog_id)
    return jsonify(products=[i.serialize for i in products])

# Admin home route
@app.route('/admin')
def adminHome():
    catalogs = CatalogModel().catalogs()
    return render_template('admin/index.html',catalogs=catalogs)

# Admin category edit route
@app.route('/admin/catalog/<int:catalog_id>', methods=['GET','POST'])
def adminCatalog(catalog_id):
    catalog = CatalogModel().catalog(catalog_id)
    if request.method == 'POST':
        CatalogModel().updateCatalog(request.form)
        catalog = CatalogModel().catalog(catalog_id)
        return render_template('admin/catalog.html',catalog=catalog)
    else:
        return render_template('admin/catalog.html',catalog=catalog)

# Admin category delete route
@app.route('/admin/catalog/<int:catalog_id>/delete', methods=['GET','POST'])
def deleteCatalog(catalog_id):
    catalog = CatalogModel().catalog(catalog_id)
    if request.method == 'POST':
        CatalogModel().deleteCatalog(catalog_id)
        return redirect("/admin")
    else:
        return render_template('admin/deleteCatalog.html',catalog=catalog)

# Admin new category route
@app.route('/admin/catalog/new', methods=['GET','POST'])
def newCatalog():
    if request.method == 'POST':
        CatalogModel().createCatalog(request.form)
        return redirect('/admin')
    else:
        return render_template('admin/newCatalog.html')


# Admin category products view
@app.route('/admin/catalog/<int:catalog_id>/products')
def adminProducts(catalog_id):
    products = ProductModel().products(catalog_id)
    catalog = CatalogModel().catalog(catalog_id)
    return render_template('admin/products.html',catalog=catalog,products=products)

# Admin products edit route
@app.route('/admin/catalog/<int:catalog_id>/product/<int:product_id>', methods=['GET','POST'])
def productView(catalog_id, product_id):
    catalog = CatalogModel().catalog(catalog_id)
    if request.method == 'POST':
        ProductModel().updateProduct(request.form)
        return redirect(url_for('adminProducts',catalog_id=catalog_id))
    else:
        product = ProductModel().product(product_id)
        catalog = CatalogModel().catalog(catalog_id)
        return render_template('admin/product.html',product=product,catalog=catalog)

# Admin product delete route
@app.route('/admin/catalog/<int:catalog_id>/product/<int:product_id>/delete', methods=['GET','POST'])
def deleteProduct(catalog_id, product_id):
    catalog = CatalogModel().catalog(catalog_id)
    if request.method == 'POST':
        ProductModel().deleteProduct(product_id)
        return redirect(url_for('adminProducts',catalog_id=catalog_id))
    else:
        product = ProductModel().product(product_id)
        catalog = CatalogModel().catalog(catalog_id)
        return render_template('admin/deleteProduct.html',catalog=catalog, product=product)

# Admin new product route
@app.route('/admin/catalog/<int:catalog_id>/product/new', methods=['GET','POST'])
def newProduct(catalog_id):
    if request.method == 'POST':
        ProductModel().createProduct(request.form)
        return redirect(url_for('adminProducts',catalog_id=catalog_id))
    else:
        return render_template('admin/newProduct.html',catalog_id=catalog_id)

# Admin user crud route
@app.route('/admin/user/<int:user_id>', methods=['GET','PUT','POST','DELETE'])
def userView(user_id):
    user = UserModel().user(user_id)
    if request.method == 'PUT':
        UserModel().updateUser(request.form)
    elif request.method == 'POST':
        UserModel().createUser(request.form)
    elif request.method == 'DELETE':
        UserModel().deleteUser(request.form['id'])
    else:
        return render_template('admin/user.html',user=user)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)