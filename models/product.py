class Product:
    def __init__(self,name,description,stock_quantity,cost,selling_price,markup,id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.cost = cost
        self.selling_price = selling_price
        self.markup = markup
        self.id = id
        