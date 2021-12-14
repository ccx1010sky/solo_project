from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manuf import Manuf
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository

manufs_blueprint = Blueprint("manufs", __name__)


# show all manufs on the web
@manufs_blueprint.route("/manufs")
def manufs():
    manufs =manuf_repository.select_all()
    return render_template("manufs/index.html", all_manufs = manufs )

# ADD_NEW
# GET '/manufs/new_manuf'
# OK
@manufs_blueprint.route("/manufs/new_manuf", methods=['GET'])
def new_manuf():
    manufs = manuf_repository.select_all()
    return render_template("manufs/new_manuf.html", all_manufs = manufs)

@manufs_blueprint.route("/manufs",methods=['POST'])
def create_manufs():
    name = request.form['name']
    info = request.form['info']
    manuf = Manuf(name,info)
    # manuf_repository.save(manuf)
    new_manuf = manuf_repository.save(manuf)
    return redirect("/manufs")

# ---------------------------------------------------



# SHOW with select id
# GET '/manufs/<id>'
# ok
# 当页面上按manuf连接时，页面上对应的manuf的id被捕捉，并执行页面上的<a href="/manufs/{{manuf.id}}">， 这个动作匹配route中的"/products/<id>"，由自定义函数show_manuf(id)来处理。
@manufs_blueprint.route("/manufs/<id>", methods=['GET'])
def show_manuf(id):
    manuf = manuf_repository.select(id)
    return render_template('manufs/show.html', manuf = manuf)


# EDIT
# GET '/products/<id>/edit'

@manufs_blueprint.route("/manufs/<id>/edit", methods=['GET'])
def edit_manuf(id):

    manuf = manuf_repository.select(id)
    return render_template('manufs/edit.html', manuf = manuf)




# UPDATE
# PUT '/manufs/<id>'
@manufs_blueprint.route("/manufs/<id>", methods=['POST'])
def update_manuf(id):
    name  = request.form['name']
    info = request.form['info']
    
    manuf = Manuf(name,info,id)
    # print(manuf.manuf.name)
    manuf_repository.update(manuf)
    return redirect('/manufs')

# ----------------------------------------------------
# DELETE
# DELETE '/manufs/<id>'
# 当页面上按delete按钮时，页面上对应的manuf的id被捕捉，并被执行action="/manufs/{{manuf.id}}/delete" method="POST" 这个动作传入下面route，由自定义函数delete_manuf(id)来处理。

@manufs_blueprint.route("/manufs/<id>/delete", methods=['POST'])
def delete_manuf(id):
    manuf_repository.delete(id)
    return redirect('/manufs')

