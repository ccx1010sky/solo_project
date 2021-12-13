import pdb
from models.product import Product
from models.manuf import Manuf
import repositories.product_repository as product_repository
import repositories.manuf_repository as manuf_repository


product_repository.delete_all()
manuf_repository.delete_all()

manuf_1 = Manuf( "manuf1","Glasgow_manuf")
manuf_2 = Manuf( "manuf2","Edinburgh_manuf")

manuf_repository.save(manuf_1)
manuf_repository.save(manuf_2)

product_1 = Product("Apple","Fruit",50,1,2,100,manuf_1)
product_2 = Product("Pear","Fruit",50,1,2,100,manuf_1)

product_repository.save(product_1)
product_repository.save(product_2)

# update table:
# product_1.name = "Grape"
# product_repository.update(product_1)

# delete table
# manuf_repository.delete(28)
# product_repository.delete(36)

# how to test method product_repository.select(id) in console.py



# print out the table as dictionary
# print(manuf_1.__dict__)
# print(manuf_2.__dict__)
# print(product_1.__dict__)
# print(product_2.__dict__)

# pdb.set_trace()