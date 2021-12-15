import unittest
from models.product import Product
from models.manuf import Manuf

class TestManuf(unittest.TestCase):
    
    def setUp(self):
        self.manuf_1 = Manuf( "manuf1","Glasgow_manuf")
        self.manuf_2 = Manuf( "manuf2","Edinburgh_manuf")
        
        # self.product_1 = Product("Apple","Fruit",50,1,2,100,manuf_1)
        # self.product_2 = Product("Pear","Fruit",50,1,2,100,manuf_1)

    
    
    def test_manuf_has_name(self):
        self.assertEqual("manuf1", self.manuf_1.name)
    def test_manuf_has_info(self):
        self.assertEqual("Edinburgh_manuf", self.manuf_2.info)
       
   