countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# count() method
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# index() method
# syntax tuple.index(element, start, end)
tuple2 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple2.index(3)
print('First occurrence of 3 is', res)

tuple3 = (0, 1, 2, 3, 2, 30, 1, 3, 2)
res = tuple3.index(3, 4,8)
print('First occurrence of 3 is', res)

print(len(tuple3))