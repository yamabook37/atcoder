N = int(input())
ans = 0
for i in range(1, N + 1):
  flg = True
  for s in str(i):
    if s == "7":
      flg = False
  for s in format(i, "o"):
    if s == "7":
      flg = False
  ans += int(flg)

print(ans)


'''
#以下pythonでは間に合わない
N = int(input())

def ok(n, a):
  while(n):
    if n % a == 7: return False
    n /= a
  return True

ans = 0
for i in range(1, N+1):
  if (ok(i,10) & ok(i,8)):
    ans += 1

print(ans)
'''