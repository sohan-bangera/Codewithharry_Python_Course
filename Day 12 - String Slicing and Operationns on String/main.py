name = "Sohan, bagera"
print(len(name))
print(name[0:5])

print(name[5])
print(name[-5])
print(name[:-1])


for len in name:
    print(len)

nm = "harry"
print(nm[-4:-2])
'''
Explanation:
the above line is print(nm[-4:-2]) can also be written as
print(nm[len(nm)-4:len(nm)-2])
print(nm[5-4:5-2])
print(nm[1:3])
which will be from 
H A R R Y
0 1 2 3 4 
the output will be from 1 to 2 
(1:3 will only work from 1 to n-1, which is 1 to 3-1 which is 1 to 2)  )
'''