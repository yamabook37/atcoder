# 2020/03/18, 26min 22:07-20:33
N=int(input())
v=[int(i) for i in input().split()]
v.sort()

for i in range(N-1):
  v[i+1] = (v[i]+v[i+1])/2
print(v[N-1])