class Item:
    pay_rate = 0.8 # discount rate of 20%

    def __init__(self, name: str, price: float , quantity = 0):
        # validations 
        assert price >= 0, f"the price {price} is not bigger than or equal to zero"
        assert quantity >= 0, f"the quantity {quantity} is not bigger than or equal to zero"
 
        # assignment
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price (self):
        return self.price * self.quantity
    


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

