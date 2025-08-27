from random import *

list = ["Aj Porate Jabo na", "Aj Porate Jabo", "Aj Pasha Khelbo", "Ekhn Ekta Ghum dibo"]

print(choice(list))

chs = choices(list, weights=[2, 10, 1, 1], k=20)
for i in chs:
    print(i)
