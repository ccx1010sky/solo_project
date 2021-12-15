import unittest
from models.product import Product
from models.manuf import Manuf

class TestManuf(unittest.TestCase):
    
    def setUp(self):
        self.manuf_1 = Manuf( "manuf1","Glasgow_manuf")
        self.manuf_2 = Manuf( "manuf2","Edinburgh_manuf")
        

    
    
    def test_manuf_has_name(self):
        self.assertEqual("manuf1", self.manuf_1.name)
    def test_manuf_has_info(self):
        self.assertEqual("Edinburgh_manuf", self.manuf_2.info)
       
   