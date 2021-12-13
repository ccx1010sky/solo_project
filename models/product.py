class Product:
    def __init__(self,name,description,stock_quantity,cost,selling_price,mark_up,manuf,id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.cost = cost
        self.selling_price = selling_price
        self.mark_up = mark_up
        self.manuf = manuf
        self.id = id


    # type of manuf is class
