'''
値xまでのN,Mの一方のみによる倍数の個数
= (Nの倍数の個数) + (Mの倍数の個数) - 2*(N,Mの最小公倍数の個数)
一方のみなので重複の差分は*2する
'''
import math
N,M,K=map(int, input().split())

# 最小公倍数 Least Common Multiple
def lcm(a, b):
  return a*b // math.gcd(a,b)

#答えは単調増加なので2分探索できる
def f(x):
    lcm_ = lcm(N, M)
    return (x // N) + (x // M) - 2*(x // lcm_)

l=0
r = 10**30
while(r-l > 1):
    
    mid = (r+l) // 2
    if f(mid) >= K:
        r = mid
    else:
        l = mid
print(r)

