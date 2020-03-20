# tttocklll さんの回答
from numpy.linalg import solve

#制約
MOD = 10**9 +7
MAX = 10**6

#　組み合わせ計算
def COM(n, r):
    fac = [1, 1]
    finv = [1, 1]
    inv = [0, 1]
    for i in range(2, MAX):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(-inv[MOD % i] * (MOD // i))
        finv.append(finv[i - 1] * inv[i] % MOD)
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD

x,y = map(int,input().split())

if (x+y)%3 != 0:
    print(0)
    exit()

l = solve([[2, 1], [1, 2]], [x, y])
if l[0] < 0 or l[1] < 0: #n,m <0の時0
    print(0)
    exit()
# n+m回のうち，どのn回で移動するか n+mCOMnを計算
print(COM(int(l[0]+l[1]), int(l[0])))
