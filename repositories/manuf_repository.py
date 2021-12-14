from db.run_sql import run_sql
from models.product import Product
from models.manuf import Manuf

# CRUD
# -------------------
# CREATE
def save(manuf):
    sql = "INSERT INTO manufs (name, info) VALUES (%s, %s) RETURNING *"
    values = [manuf.name, manuf.info]
    results = run_sql(sql, values)
    id = results[0]['id']
    manuf.id = id
    return manuf

# -----------------------------------------------
# READ
def select_all():
    manufs = []

    sql = "SELECT * FROM manufs"
    results = run_sql(sql)

    for row in results:
        manuf = Manuf(row['name'], row['info'], row['id'] )
        manufs.append(manuf)
    return manufs
# READ
def select(id):
    manuf = None
    sql = "SELECT * FROM manufs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manuf = Manuf(result['name'], result['info'], result['id'] )
    return manuf

# -----------------------------------------
# UPDATE
def update(manuf):
    sql = "UPDATE manufs SET (name, info) = (%s, %s) WHERE id = %s"
    values = [manuf.name, manuf.info, manuf.id]
    run_sql(sql, values)

# -----------------------------------
# DELETE
def delete_all():
    sql = "DELETE  FROM manufs"
    run_sql(sql)

# DELETE
def delete(id):
    sql = "DELETE  FROM manufs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# _______________________________

# 显示某个manuf下的所有产品
def products(manuf):
    products = []

    sql = "SELECT * FROM products WHERE manuf_id = %s"
    values = [manuf.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['cost'],row['selling_price'],row['mark_up'], row['manuf_id'], row['id'] )
        products.append(product)
    return products
