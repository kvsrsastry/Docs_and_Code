import yaml

ds = {'ganesh':{'kvsr':[1,2,3.4]}, 'k1': {'k2': [1,2,3]}}

with open('yaml_out.yaml', 'w') as fh:
    yaml.dump(ds, fh, default_flow_style=False)

with open('yaml_out.yaml') as fh:
    ds1 = yaml.load(fh)
    print(ds1)
    print(type(ds1))

