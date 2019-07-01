t = ('ganesh',) # Tuple with single element. Please note the comma at the end
print(type(t))
print(t)
a, b, c = (33, 44, 22) # Tuple unpacking
d = (77)
print(a,b,c,d,sep='%')
t = t + (1,2,3, 'ganesh') # Tuples are immutable. You just have to re-assign them with new values
print(t)
print(t.count('ganesh'))
print(t.index('ganesh'))
print(t.index('ganesh', 1))
