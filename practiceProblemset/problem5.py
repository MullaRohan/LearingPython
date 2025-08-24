n = int(input())
dic = {}
for _ in range(n):
    key, val = input().split()
    dic[key] = int(val)
fnd = input()
if fnd in dic.keys():
    print(dic[fnd])
else:
    print("Not Found")
