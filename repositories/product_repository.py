

from db.run_sql import run_sql

from models.Product import Product
from models.manuf import Manuf


# 
def save(product):
    sql = "INSERT INTO products (name, descriptioin, stock_quantity, cost,selling_prince,mark_up,manuf_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.descriptioin, product.stock_quantity, product.cost,product.cost,product.selling_price,product.mark_up,product.manuf_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


