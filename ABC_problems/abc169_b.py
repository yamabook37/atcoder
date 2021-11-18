N=int(input())
A = list(map(int,input().split()))
#print(A[0])
if 0 in A:
  print('0')
  exit()

ans = 1 
for i in range(N):
  ans *= A[i]
  if ans > 1e+18:
    print('-1')
    exit()
print(ans)