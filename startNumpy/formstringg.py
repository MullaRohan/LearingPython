import numpy as np

s = np.fromstring(input(), dtype= "int64", sep=" ")

for x in s:
    print(x)

print("dype", s.dtype)