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

