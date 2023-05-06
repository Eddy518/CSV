from item import Item


item1=Item("myItem", 750)
item2=Item("item2", 500)

#setting an attribute
item1.name="OtherItem"

#getting an attribute
print(item1.name)

print(item2.name)


print(item2.apply_increment(0.2))
