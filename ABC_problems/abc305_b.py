import math

p, q = input().split()
dif=[0,3,1,4,1,5,9]
node=[3,4,8,9,14,23]

#unicode
p = ord(p)-ord('A')
q = ord(q)-ord('A')

res = 0
if p > q:
    p = p ^ q
    q = p ^ q
    p = p ^ q
i = p + 1
while i <= q:
    res += dif[i]
    i+=1
print(res)