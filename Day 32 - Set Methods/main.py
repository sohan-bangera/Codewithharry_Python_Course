s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1)

print(s1.union(s2))
print(s1.intersection(s2))

#update()
s1.update(s2)

print(s1)

#intersection
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#intersection_Update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)

#symmetric_Difference
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
s3 = s1.symmetric_difference(s2)
print(s3) 

print(s2.difference(s1))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


s1.discard(32)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")