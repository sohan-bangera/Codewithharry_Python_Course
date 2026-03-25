info = {'name':'Sohan','Age':25, 'eligible':True}
print(info)
info.update({'Age':26})
info.update({'DOB':2001})
print(info)

# info.clear()
# print(info)

info.popitem()

print(info)