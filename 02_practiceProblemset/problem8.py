#prefix sum
n = int(input())
list1 = list(map(int, input().split()))
x = 0
for i in list1:
    print(i+x,end=" ")
    x += i