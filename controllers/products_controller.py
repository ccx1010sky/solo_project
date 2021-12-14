from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository

products_blueprint = Blueprint("products", __name__)



# 总结：route的第一个参数与form中的action对应，或与href中的连接对应。
# id等参数由html中传入到controller.py中

# show all products on the web
@products_blueprint.route("/products")
def products():
    products =product_repository.select_all()
    return render_template("products/index.html", all_products = products )

# ADD_NEW
# GET '/products/new_product'
# OK
@products_blueprint.route("/products/new_product", methods=['GET'])
def new_product():
    manufs = manuf_repository.select_all()
    return render_template("products/new_product.html", all_manufs = manufs)
    # return render_template("manuf/index.html", all_manufs = manufs)

# OK
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
# -----------------------------------------------------

# SHOW
# GET '/products/<id>'
# ok
# 当页面上按product连接时，页面上对应的product的id被捕捉，并执行页面上的<a href="/products/{{product.id}}">， 这个动作匹配route中的"/products/<id>"，由自定义函数show_product(id)来处理。
@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)


# EDIT
# GET '/products/<id>/edit'

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufs = manuf_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufs = manufs)

# -----------------------------------------------------

# UPDATE
# PUT '/products/<id>'
@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name  = request.form['name']
    description = request.form['description']
    stock_quantity   = request.form['stock_quantity']
    cost   = request.form['cost']
    selling_price   = request.form['selling_price']
    mark_up   = request.form['mark_up']
    manuf = manuf_repository.select(request.form['manuf_id'])
    product = Product(name,description,stock_quantity,cost,selling_price,mark_up,manuf, id)
    print(product.manuf.name)
    product_repository.update(product)
    return redirect('/products')

# DELETE
# DELETE '/products/<id>'
# 当页面上按delete按钮时，页面上对应的product的id被捕捉，并被执行action="/products/{{product.id}}/delete" method="POST" 这个动作传入下面route，由自定义函数delete_product(id)来处理。

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')





