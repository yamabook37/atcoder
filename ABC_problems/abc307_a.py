n = int(input())
a = list(map(int, input().split()))
#print(a)
for i in range(n):
    sum=0
    for j in range(7):
        sum += a[7*i + j]
    if i != n-1:
        print(sum, end=" ")
        #続きあり
    else:
        print(sum, end="\n")