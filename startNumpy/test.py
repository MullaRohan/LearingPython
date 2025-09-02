import numpy as np

s = np.array(list(map(int,input().split())), dtype='int64')

for _ in range(0,len(s), 1):
    print(s[_])
print("dtype", s.dtype)