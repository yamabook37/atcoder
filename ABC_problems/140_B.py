# 2019/11/17 20min

n = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
#print(C) #Cはn-1こなことに注意

b = sum(B)
for i in range(n-1):
    if A[i]+1 == A[i+1]:
        b += C[A[i]-1]
print(b)

'''
3
3 1 2
2 5 4
3 6

4
2 3 4 1
13 5 8 24
45 9 15

2
1 2
50 50
50
'''