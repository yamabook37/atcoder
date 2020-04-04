# 2020/3/21 6:43-49, 6min
N=int(input())
L=[int(i) for i in input().split()]
long=max(L)
#print(long)
L.remove(long)
if long<sum(L):
  #print(sum(L))
  print('Yes')
else:
  print('No')