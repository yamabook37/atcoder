N,K=map(int,input().split())
MOD=int(1e9)+7

dp=[0]*(K+1)
for i in range(K):
  j=K-i
  dp[j]+=pow(K//j, N, MOD)

  k=2*j
  while k<=K:
    dp[j]=(dp[j]-dp[k]+MOD) % MOD
    k+=j

ans=0
for i in range(1,K+1):
  ans+=dp[i]*i
  ans%=MOD
print(ans)


# DP使って、はじめてE通せたーーー！感無量