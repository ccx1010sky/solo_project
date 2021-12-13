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

@products_blueprint.route("/products/new_product")
def create_products():
    name = request.form['name']
    description = request.form['description']
    stock_quantity = request.form['stock_quantity']
    cost = request.form['cost']
    selling_price = request.form['selling_price']
    mark_up = request.form['mark_up']
    # 
    manuf = manuf_repository.select(request.form['manuf_id'])

    new_product = product_repository.save()
    return render_template("products/index.html", all_products = products )




