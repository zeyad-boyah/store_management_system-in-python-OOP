import csv

class Item:
    pay_rate = 0.8 # discount rate of 20%
    all = [] # this list will contain every generated item

    def __init__(self, name: str, price: float , quantity = 0):
        # validations 
        assert price >= 0, f"the price {price} is not bigger than or equal to zero"
        assert quantity >= 0, f"the quantity {quantity} is not bigger than or equal to zero"
 
        # assignment
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions
        Item.all.append(self) 
    
    def calculate_total_price (self):
        return self.price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('store_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        # initiate each item from the file to the class 
        for item in items:
            Item(
                name= item["name"],
                price=float(item["price"]),
                quantity= int(item["quantity"])     
            )

    
    def __repr__(self):
        return F"Item '{self.name}', '{self.price}', '{self.quantity}'."
    

Item.instantiate_from_csv()
print(Item.all)

