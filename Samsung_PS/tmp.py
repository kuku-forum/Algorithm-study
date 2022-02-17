from copy import deepcopy
from re import A

a = {0: 1, 2: 4}

b = deepcopy(a)

print(a)
print(b)

b[0] += 1

print(a)
print(b)