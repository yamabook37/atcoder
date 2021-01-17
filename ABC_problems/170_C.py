import math

x, n = map(int, input().split())
p = list(map(int, input().split()))

ans = -1
dif = 10000
for i in range(102):
  if i in p: #含まれている時
    continue
  else:
    if abs(x - i) < dif:
      ans = i
      dif = abs(x - i)

print(ans)

'''
6 5
4 7 10 6 5
'''
