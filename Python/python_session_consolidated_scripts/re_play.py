import re

master_str = 'ganesh is the pratham pujya'

# Checking for contains as well as CASE-INSENSITIVITY
if re.search('\s+THE\s+', master_str, re.I):
    print(True)
else:
    print(False)

match_object = re.search('(.*) (.*)', master_str)
if match_object:
    print(match_object.groups())
    print(match_object.span())

print(re.findall('\w+', master_str))
