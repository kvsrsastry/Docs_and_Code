# map, reduce, filter, ord, chr, bin, hex, abs, pow, round, sqrt, int, random.randint, random.shuffle etc.
l = [1,2,3,4,5]

# map
mapped_l = map(lambda x: x ** 3, l)
print(list(mapped_l))

# filter
filtered_l = filter(lambda x: x % 2 == 0, l)
print(list(filtered_l))

# reduce
from functools import reduce
summ = reduce(lambda x,y: x+y, l, 0)
print(summ)

# ord
print(ord('A'))

# chr
print(chr(65))

# bin
print(bin(15))

# hex
print(hex(15))

# abs
print(abs(-34))

# pow
print(pow(3,4))
print(pow(3,4,8))  # equal to (3 ** 4) % 8

# round
import math
print(round(math.pi, 4))

# sqrt and int
print(int(math.sqrt(9)))

# random.randint and random.shuffle
import random

print(random.randint(0,3))
print(l)
random.shuffle(l)
print(l)
