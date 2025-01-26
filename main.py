from item import Item
from phone import Phone

Item.instantiate_from_csv()
phone1 = Phone("galaxy phone 1", 500, 5, 1)
print(phone1.price)
phone1.apply_discount() 
print(phone1.price)


item1 = Phone.all[1]
print(item1.price)
item1.apply_discount()
print(item1.price)
print(Phone.all)
