N, K, A = map(int, input().split())
ans = 0

# N=1では1に決定
if N == 1:
  ans = 1
  print(ans)
  exit()
  
ans = (A+K-1) % N
if ans == 0:
  print(N)
else:
  print(ans)