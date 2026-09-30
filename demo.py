class Clothing:
    def __init__(self, type, color, size, price=None):
        self.type = type
        self.color = color
        self.size = size
        self.price = price

    def set_price(self, price):
        # Set the price of an item of clothing.
        self.price = price
        print(f"Setting the price of the {self.color} {self.type} to ${price}.")

    def get_price(self):
        # Get the price of an item of clothing, if price is set.
        try:
            assert self.price != None
            print(f"The {self.color} {self.type} costs ${self.price}.")
        except:
            print(f"The price of the {self.color} {self.type} hasn't been set yet!")
    
    def promote(self, percentage):
        # Lower the price, if initial price is set.
        try:
            self.price = self.price * (1-percentage/100)
            print(f"The price of the {self.color} {self.type} has been reduced by {percentage} percent! It now only costs ${self.price:.0f}.")
        except:
            print(f"Oops. Set an initial price first!")

bluejeans = Clothing("jeans", "blue", 34)

redTshart = Clothing("T_shart","red",32)

