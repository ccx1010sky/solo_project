from db.run_sql import run_sql
from models.product import Product
from models.manuf import Manuf
import repositories.manuf_repository as manuf_repository



def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, cost,selling_price,mark_up,manuf_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.cost,product.selling_price,product.mark_up,product.manuf.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def delete_all():
    sql = "DELETE  FROM products"
    run_sql(sql)

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manuf = manuf_repository.select(row['manuf_id'])
        product = Product(row['name'], row['description'], row['stock_quantity'], row['cost'],row['selling_price'],row['mark_up'],manuf,row['id'] )
        products.append(product)
    return products



def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manuf = manuf_repository.select(result['manuf_id'])
        product = product(result['name'], result['description'], result['stock_quantity'], result['cost'],result['selling_price'],result['mark_up'],manuf,result['id'] )
    return product


def delete(id):
    sql = "DELETE  FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, cost,selling_price,mark_up,manuf_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock_quantity,product.cost,product.selling_price,product.mark_up,product.manuf.id, product.id]
    print(values)
    run_sql(sql, values)