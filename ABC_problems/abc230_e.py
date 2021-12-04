n = int(input())

#探索の上限を設定
k=0
for i in range(1,n+1):
  if (i*i <= n):
    k=i
  else:
    break

#解説の二項を計算
ans=0
for i in range(1, k+1):
  ans += ((n // i) - (n // (i + 1)))*i
for i in range(1,(n // (k + 1))+1):
  ans += n//i
  
print(ans)