#094_B 10min
N,M,X=map(int,input().split())
A=[int(i) for i in input().split()]
#print(A)
left=0
right=0
#通過した数をカウント
for i in A:
  if i>X:
    right+=1 #右端へ移動
  else:
    left+=1
ans=min(left,right)
print(ans)