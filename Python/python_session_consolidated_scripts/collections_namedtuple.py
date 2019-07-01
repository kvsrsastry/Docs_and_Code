from collections import namedtuple

god = namedtuple('god', 'name wifename kiddo')
t1 = god('shiva', 'parvathi', 'ganesh')
print(t1.name) # Access by attr name
print(t1[0])   # Access by index 
print(t1.wifename)
