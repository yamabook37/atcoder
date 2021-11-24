K, N = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.append(A[0]+K)
dif = 0
for i in range(1, N+1):
  dif = max(dif, A[i] - A[i-1])
  #print(dif)
print(K-dif)
