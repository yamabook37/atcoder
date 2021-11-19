# 解説AC
# https://atcoder.jp/contests/abc227/editorial/2928
# 決め打ち二分探索

N, K = map(int,input().split())
A = [int(i) for i in input().split()]

# 「x 個のプロジェクトを作れる」ことの必要十分条件
def condition(x):
  res = 0
  for i in range(N):
    res += min(A[i],x)
  return res >= K*x

ok,ng = 0,10**20
while ng-ok > 1:
  m = (ok+ng)//2
  if condition(m):
    ok = m
  else:
    ng = m
    
print(ok)