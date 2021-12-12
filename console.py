from models.product import Product
from models.manuf import Manuf
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository


product_repository.delete_all()
manuf_repository.delete_all()

manuf1 = Manuf( "manuf1","glasgow_manuf")
manuf_repository.save(manuf1)

product1 = Product("Apple","Fruit",50,1,2,100,manuf1)
product_repository.save(product1)