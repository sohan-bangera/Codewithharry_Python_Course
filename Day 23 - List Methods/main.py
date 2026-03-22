l = [3,8,12,1,2,4,6]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)

# this is a wrong way of doing as this will change the value in the L list too not just m
# m = l
# m[0] = 0
# print(l)


#make use of copy() method to copy from L and keep the L list unaffected
n = l.copy()
n[0] = 0
print(l)

k = [1,2,3]
o = [4,5,6]
k.extend(o)
print(k)
'''
k => [1,2,3].extend([4,5,6])
k => [1,2,3] + [4,5,6]
k => [1,2,3,4,5,6] <- final result
'''

k.pop()
print(k)