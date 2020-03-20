# 2019/11/17 3min

n,k = map(int, input().split())
lis = [int(i) for i in input().split()]
a=[]

for i in range(n):
    if lis[i]>=k:
        a.append(lis[i])

print(len(a))