import math
def comb(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

L = int(input())
ans = comb(L-1, 11)
print(ans)


'''
# python3.8.2
from math import comb

L = int(input())
ans = comb(L-1, 11)
print(ans)
'''

'''
L = int(input())

res = 1
for i in range(1,11+1):
  res *= (L-i)
  res /= i

print(int(res))
# これだとオーバーフローしてる？
'''
