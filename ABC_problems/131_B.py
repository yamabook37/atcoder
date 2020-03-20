# 2020/03/18, 32min 19:44-20:18
N,L = map(int,input().split())
aji = [L+i for i in range(N)]
#print(aji)
total = sum(aji)
#print(total)

eat = 1000
j=0
for i in range(N):
  if eat > abs(aji[i]):
    eat = abs(aji[i])
    # eat  は正の値

if min(aji) >0:
  print(total-eat)
else:
  print(total+eat)

