import unittest
from models.product import Product
from models.manuf import Manuf

class TestProdcut(unittest.TestCase):
    
    def setUp(self):
        self.manuf_1 = Manuf( "manuf1","Glasgow_manuf")
        self.manuf_2 = Manuf( "manuf2","Edinburgh_manuf")
        
        self.product_1 = Product("Apple","Fruit",50,1,2,100,manuf_1)
        self.product_2 = Product("Pear","Fruit",50,1,2,100,manuf_1)

    
    
    def test_product_has_name(self):
        self.assertEqual("Apple", self.product_1.name)
       
    def test_product_has_description(self):
        self.assertEqual("Fruit", self.product_1.description)
        
        
        
    def test_product_has_stock_quantity(self):
        self.assertEqual(50, self.product_1.stock_quantity)
    
    
    def test_product_has_cost(self):
        self.assertEqual(1, self.product_1.cost)
        
    
