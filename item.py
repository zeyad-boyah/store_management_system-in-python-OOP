import csv
from os import name


class Item:
    pay_rate = 0.8  # discount rate of 20%
    all = []  # this list will contain every generated item

    def __init__(self, name: str, price: float, quantity=0):
        # validations
        assert price >= 0, f"the price {price} is not bigger than or equal to zero"
        assert (
            quantity >= 0
        ), f"the quantity {quantity} is not bigger than or equal to zero"

        # assignment
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def price_increment(self,value):
        self.__price = self.__price * value

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("store_data.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        # initiate each item from the file to the class
        for item in items:
            Item(
                name=item["name"],
                price=float(item["price"]),
                quantity=int(item["quantity"]),
            )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @staticmethod
    def is_integer(num):

        if isinstance(num, float):
            # this will only return true if the first decimal is only 0 ex: 5.0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}', '{self.__price}', '{self.quantity}'."
