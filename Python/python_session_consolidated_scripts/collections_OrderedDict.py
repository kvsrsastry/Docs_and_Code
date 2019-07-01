from collections import OrderedDict

d1 = OrderedDict()
d1['k1'] = 1
d1['k2'] = 2
d1['k5'] = 5
d1['k4'] = 4
d1['k3'] = 3

# OrderedDict Prints in the order we have incorporated key/value pairs in the dict
# Normal Dictionary may nor print it in the order
print('Ordered Dict')
for k, v in d1.items():
    print(k,v)

