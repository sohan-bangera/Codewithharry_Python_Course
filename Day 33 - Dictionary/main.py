dic = {
    "Name":"Sohan",
    "Age":25,
    "Gender":"Male"
}

#Difference between dic['Name] and dic.get['Name']
#dic['Name'] will give error if key does not exist
#but dic.get['Name'] will give "None" if the key does not exist
print(dic['Name'])
print(dic.get('Name'))
print(dic)
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(dic[key])

print(dic.items())

for key, value in dic.items():
    print(f"The {key} is {value}")