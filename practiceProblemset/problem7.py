# st1 = input()
# st2 = input()

# dic1 = {}
# dic2 = {}
# for i in st1:
#     dic1[i] = dic1.get(i, 0) + 1
# for i in st2:
#     dic2[i] = dic2.get(i, 0) + 1

# ans = True

# for key in dic1.keys():
#     if dic1[key] != dic2.get(key, 0):
#         ans = False
# if ans:
#     print("YES")
# else:
#     print("NO")


from collections import Counter
str1 = input()
str2 = input()
if Counter(str1) != Counter(str2):
    print("NO")
else:
    print("YES")