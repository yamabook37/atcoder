from itertools import accumulate
import math
import fractions

N = int(input())
A = [int(i) for i in input().split()]

#最大公約数で累積和作る
B = [0] * (N+1)
R = [0] * (N+1)
for i in range(N):
    B[i+1] = (fractions.gcd(B[i],A[i]))
    #逆向き,とったやつの反対端用   
    R[N-i -1] = (fractions.gcd(R[N-i], A[N-1 -i]))
 
ans = 0
for i in range(N):
    ans = max(ans, fractions.gcd(B[i], R[i+1]))
print(ans)

'''
3
7 6 8
'''