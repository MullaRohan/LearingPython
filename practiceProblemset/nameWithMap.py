n = int(input())

list1 = input().split()
dic = {}

for i in list1:
    dic[i] = dic.setdefault(i, 0) + 1

for i, j in sorted(dic.items()):
    print(i,j)