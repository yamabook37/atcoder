import itertools
import math

N,M=map(int,input().split())
ans = 0
even = 0
odd = 0
if N > 1:
    even += math.factorial(N) / (math.factorial(2)*math.factorial(N - 2))
if M > 1:
    odd += math.factorial(M) / (math.factorial(2)*math.factorial(M - 2))
ans=even+odd
print(int(ans))