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

"""
Admin Routes
    1. home: renders the admin dashboard    www.site.com/dashboard
    2. User: update user information        www.site.com/dashboard/user
    3. Models: update database information  www.site.com/dashboard/models
    4. Category: CRUD for categories        www.site.com/dashboard/category
    5. Product: CRUD for products           www.site.com/dashboard/product
"""


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)