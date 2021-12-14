from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manuf import Manuf
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository

manufs_blueprint = Blueprint("manufs", __name__)


# show all manufs on the web
@manufs_blueprint.route("/manufs" , methods=['GET'])
def manufs():
    manufs =manuf_repository.select_all()
    return render_template("manufs/index.html", all_manufs = manufs )