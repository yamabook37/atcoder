import math

n, d=map(int, input().split())
x=[]
for i in range(n):
    x.append([int(i) for i in input().split()])

ans=0
for i in range(n-1): #0-n
  for j in range(i+1,n):
    s = 0
    for k in range(d):
      s += (x[i][k]-x[j][k])**2
    a = math.sqrt(s)
    if a.is_integer():
      ans += 1
print(ans)