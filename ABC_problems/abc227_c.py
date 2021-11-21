N=int(input())

ans=0
# A,B,Cの順に決めていく全探索
for A in range(1, N+1):
  # ans=0の例外
  if A*A*A > N: break

  # A <= B
  for B in range(A, N+1):
    if A*B*B > N: break
  
    C = N//(A*B)
    ans += C -B+1
# O(N^2/3)
# 1<=N<=10^11 Python3.8ではTLE, PyPy3.7で提出する

print(ans)