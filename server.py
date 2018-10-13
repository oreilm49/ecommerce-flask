from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from model import ProductModel, CatalogModel, UserModel

app = Flask(__name__)


# Home route
@app.route('/')
def index():
    catalogs = CatalogModel().catalogs()
    return render_template('index.html',catalogs=catalogs)

# Category page
@app.route('/<category>/items')
def categoryCatalog(category):
    products = ProductModel().products(category)
    return render_template('category.html',category=category,products=products)

# Product page
@app.route('/<category>/product/<int:id>')
def productPage(category, id):
    product = ProductModel().product(id)
    return product

# Products JSON
@app.route('/<category>/items/JSON')
def categoryCatalogJSON(category):
    products = ProductModel().products(category)
    return jsonify(products=[i.serialize for i in products])

# Admin home route
@app.route('/admin/<int:user_id>', methods=['GET','PUT','POST','DELETE'])
def adminHome(user_id):
    catalogs = CatalogModel().catalogs()
    if request.method == 'PUT':
        CatalogModel().updateCatalog(request.form)
    elif request.method == 'POST':
        CatalogModel().createCatalog(request.form)
    elif request.method == 'DELETE':
        CatalogModel().deleteCatalog(request.form['id'])
    else:
        return render_template('index.html',catalogs=catalogs)

# Admin category products view
@app.route('/admin/<category>/products')
def adminProducts(category):
    products = ProductModel().products(category)
    return render_template('admin/category.html',products=products)

# Admin products crud route
@app.route('/admin/product/<int:product_id>', methods=['GET','PUT','POST','DELETE'])
def productView(product_id):
    product = ProductModel().product(product_id)
    if request.method == 'PUT':
        ProductModel().updateProduct(request.form)
    elif request.method == 'POST':
        ProductModel().createProduct(request.form)
    elif request.method == 'DELETE':
        ProductModel().deleteProduct(request.form['id'])
    else:
        return render_template('admin/product.html',product=product)

# Admin products crud route
@app.route('/admin/product/<int:user_id>', methods=['GET','PUT','POST','DELETE'])
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