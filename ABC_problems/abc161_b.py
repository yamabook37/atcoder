N,M=map(int,input().split())
A=[int(b) for b in input().split()]
cnt=0
ans=sum(A)/(4*M)
#print(ans)

for i in range(N):
  if A[i] >=ans: #未満は選べない，以上を選ぶ(最後のケース)
    cnt+=1
#print(cnt)

if cnt >= M:
  print('Yes')
else: print('No')
