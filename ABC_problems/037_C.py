from itertools import accumulate

N, K= map(int,input().split())
A = [int(i) for i in input().split()]

B = [0] + A
B = list(accumulate(B))
#print(B)

ans =0
for i in range(K, N+1):
    ans += B[i] - B[i-K]
print(ans)

'''
5 3
1 2 4 8 16
'''