from db.run_sql import run_sql
from models.product import Product
from models.manuf import Manuf


def save(manuf):
    sql = "INSERT INTO manufs (name, info) VALUES (%s, %s) RETURNING *"
    values = [manuf.name, manuf.info]
    results = run_sql(sql, values)
    id = results[0]['id']
    manuf.id = id
    return manuf


def delete_all():
    sql = "DELETE  FROM manufs"
    run_sql(sql)