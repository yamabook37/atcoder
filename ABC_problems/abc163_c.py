# ここまで15min
N=int(input())
A=list(map(int, input().split()))
cnt=[0]*N

for i in range(N-1):
  cnt[A[i]-1] += 1

for j in range(N):
  print(cnt[j])


'''
N=int(input())
A= [int(i) for i in input().split()]
A.sort()
for i in range(1,N+1):
  ans=A.count(i)
  print(ans)
'''
