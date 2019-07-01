import json

ds = ['ganesh', {'k1': {'k2': [1,2,3]}}, 'a', 13.4, 15]

print(json.dumps(ds)) # Dump as a string to screen

# Dump the DataStructure to a File
with open('json_out.json', 'w') as fh:
    json.dump(ds, fh)

# Load the json from the File to Memory
ds1 = None
with open('json_out.json') as fh:
    ds1 = json.load(fh)

print(ds1)

with open('json_out.json') as fh:
    for line in fh:
        print(json.loads(line))
        print(type(json.loads(line)))

class jclass():
 def __init__(self, name, age):
  self.name = name
  self.age = age

def jdefault(obj):
 return obj.__dict__

j1 = jclass('ganesh', 37)
print(json.dumps(j1, default=jdefault))

