N=int(input())
V=list(int(i) for i in input().split())
C=list(int(i) for i in input().split())

ans=0
for i in range(N):
  if V[i]>C[i]:
    ans += V[i]-C[i]
print(ans)