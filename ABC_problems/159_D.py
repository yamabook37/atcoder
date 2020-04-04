import collections
import math

def comb(n, r):
  if n < r:
      return 0
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N=input()
A = list(map(int, input().split()))
c = collections.Counter(A)
#print(c.values())

ans = sum([comb(v, 2) for v in c.values()])
for ai in A:
    print(ans - c[ai] + 1)
