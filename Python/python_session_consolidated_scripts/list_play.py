l = ['ganesh', 1, 2, 3, 'v', 34.7]
l1 = list() # Calling the List Class Constructor
print(type(l))
print(type(l1))
l1.append('ganesh')
l1.extend([1,2,3])
print(l1)
g1 = l1.pop()
print(l1)
g2 = l1.pop(0)
print(l1)
l1.insert(0,'ganesh')
print(l1)
print(len(l1))
if(l1.count(2) > 0):
 print(l1.index(2))
if(l1.count(4) > 0):
 print(l1.index(4))
if(l1.count('ganesh') > 0):
 l1.remove('ganesh')
print(l1)
l1.insert(0,'ganesh')
l1.extend([3, 'v', 234, 34.7])
print(l1)
del(l1[5])
print(l1)
print(l == l1)
