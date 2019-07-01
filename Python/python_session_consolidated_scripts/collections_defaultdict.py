from collections import defaultdict

d = defaultdict(lambda: 1)
print(d['one'])   # It will not give KeyError even though key 'one' is not present before
                  # If it is normal dict, it will throw KeyError Exception

