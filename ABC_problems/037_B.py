N,Q=map(int,input().split())
A=[0]*(N)

for i in range(Q):
  L,R,T=map(int,input().split())
  for j in range(L, R+1):
    A[j-1]=T
    #print(A)
    
#print(A)
for i in range(N):
  print(A[i])