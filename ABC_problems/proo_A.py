from itertools import accumulate

N = int(input())
A = [int(i) for i in input().split()]

B = [0] + A
B = list(accumulate(B))

ans =[]
for i in range(1, N+1):
    ans = max([B[i+k]-B[k] for k in range(N-i+1)])
    print(ans)

'''
4
4 1 3 3

5
10 20 30 40 50
'''