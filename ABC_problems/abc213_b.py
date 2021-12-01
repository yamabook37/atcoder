N=int(input())
A=list(map(int,input().split()))

v=[]
# インデックスを保持したいのでタプルにする
for i in range(N):
	v.append((A[i],i+1))
# 降順にソート
v.sort()
v.reverse()
print(v[1][1])