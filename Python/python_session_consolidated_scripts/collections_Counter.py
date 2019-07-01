from collections import Counter

# character count in a string
st = 'this is the rythm of the life'
c1 = Counter(st)
print(c1)
print(c1.most_common()[:-3:-1])

# item count in a list
l = [1,2,2,2,2,3,33,3,3]
c2 = Counter(l)
print(c2.most_common(3))
d = dict(c2)
print(d)

# Word count in a String
st = 'the the the is the are the give me the'
l1 = st.split()
c3 = Counter(l1)
print(c3.most_common(2))
d2 = dict(c3)
print(d2)
