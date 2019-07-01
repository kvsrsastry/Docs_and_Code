d = dict() # Calling the Constructor
print(type(d))
d = {'k3' : 33, 'k1': 22, 'k2': 11}
print(d.keys())
print(d.values())
for k,v in sorted(d.items(), key=lambda t: t[1], reverse=True):
    print(k,v,sep=' -> ')
print(d['k3'])
print('k2' in d)
for k in sorted(d.keys()):
    print(k, d[k],sep=' -> ')
