from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity=0, broken_phones: int = 0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones aren't bigger than or equal to zero"

        self.broken_phones = broken_phones
