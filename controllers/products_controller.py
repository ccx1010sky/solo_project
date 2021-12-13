from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository

products_blueprint = Blueprint("products", __name__)

# show all products on the web
@products_blueprint.route("/products")
def products():
    products =product_repository.select_all()
    return render_template("products/index.html", all_products = products )

# NEW
# GET '/products/new'
@products_blueprint.route("/products/new_product", methods=['GET'])
def new_book():
    manufs = manuf_repository.select_all()
    return render_template("products/new_product.html", all_manufs = manufs)


@products_blueprint.route("/products",methods=['POST'])
def create_products():
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    cost = request.form['cost']
    selling_price = request.form['selling_price']
    mark_up = request.form['mark_up']
    # 
    manuf = manuf_repository.select(request.form['manuf_id'])
    product = Product(name,description,stock_quantity,cost,selling_price,mark_up,manuf)
    product_repository.save(product)

    new_product = product_repository.save(product)
    return redirect("/products")

# SHOW
# GET '/products/<id>'
@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

# EDIT
# GET '/products/<id>/edit'
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_book(id):
    product = product_repository.select(id)
    manufs = manuf_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufs = manufs)





