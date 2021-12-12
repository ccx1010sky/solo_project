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