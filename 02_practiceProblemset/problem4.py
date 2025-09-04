# # process 1
# n = int(input())

# list1 = list(map(int, input().split()))
# dic = {}
# for i in list1:
#     dic[i] = dic.get(i, 0) + 1
# for i in sorted(dic.keys()):
#     print(i, end=" ")

# process 2

n = int(input())

list1 = list(map(int, input().split()))
st = set()
for i in list1:
    st.add(i)
for i in st:
    print(i,end=" ")