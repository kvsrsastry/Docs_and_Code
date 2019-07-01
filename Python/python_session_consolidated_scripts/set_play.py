s = set() # Calling the Set Class Constructor
s = set(range(10))
print(type(s))
print(s)
s.add(10)
print(s)
s.discard(10)
s.add(9) # Already element 9 is present. Set will maintain only one copy of any element
print(s)
s1 = set(range(6,14))
print(s1)
print(s.union(s1)) # UNION
#s.update(s1)       # UNION UPDATE
#print(s)

print(s.intersection(s1)) # INTERSECTION
#s.intersection_update(s1) # INTERSECTION UPDATE
#print(s)

print(s.difference(s1)) # DIFFERENCE (S - S1)
#s.difference_update(s1) # DIFFERENCE UPDATE
#print(s)

print(s.symmetric_difference(s1)) # (S - S1) UNION (S1 - S)
#s.symmetric_difference_update(s1) # SYMMETRIC DIFFERENCE UPDATE
#print(s)

scopy = s.copy()
print(scopy)
print(len(scopy))
print(scopy.issubset(s))
print(s.issuperset(scopy))
print(s.isdisjoint(scopy))
s.clear()
print(s)
s = set('ganesh maharaj')
print(s)
