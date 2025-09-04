n = int(input())

mList = list(map(int, input().split()))
dic = {}
for i in mList:
    dic[i] = dic.get(i, 0) + 1

maxFreq = max(dic.values())
numbers = []
for key, val in dic.items():
    if val == maxFreq:
        numbers.append(key)

print(f"{min(numbers)} -> {maxFreq}")