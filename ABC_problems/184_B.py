N,X = map(int,input().split())
S = input()

ans = X

for s in S:
  if s == 'x' and ans > 0:
    ans -= 1
  elif s == 'o':
    ans += 1
print(ans)
