from numpy import *

ls1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
#             0   1  2   3    4   5   6   7   8    9
ls2 = ls1[:3]
ls3 = ls1[5:]
ls4 = ls1[2:5]

print(ls1)
print(ls2)
print(ls3)
print(ls4)


print(ls4[1])

ls5 = ls1
print(ls5)