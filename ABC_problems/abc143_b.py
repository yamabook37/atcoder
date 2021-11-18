# 2019/11/17 7min

n = int(input())
lis = [int(i) for i in input().split()]
#print(lis)
way = 0

for i in range(n):
    for j in range(n):
        if i<j:
            way += lis[i]*lis[j]
print(way)

'''
7
5 0 7 8 3 3 2
'''