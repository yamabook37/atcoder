#Pypyで提出...時間かかりそう
# というか全部Pypyで出せばいい

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

K=int(input())
ans=0
for i in range(1,K+1):
  for j in range(1,K+1):
    for k in range(1,K+1):
      ans += gcd(i,j,k)
#print(len(ans))
print(ans)