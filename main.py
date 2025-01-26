from item import Item
from phone import Phone

Item.instantiate_from_csv()
phone1 = Phone("susphone1", 500, 5, 1)
phone1.name = "sus"
print(Phone.all)
