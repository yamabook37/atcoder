n = int(input())
t = [0]*(n+1)
k = [0]*(n+1)
a = [0]*(n+1)

# 1indexなので初期値を1ずらす
for i in range(1, n+1):
  inp = list(map(int,input().split()))
  t[i] = inp[0]
  k[i] = inp[1]
  a[i] = inp[2:]
  #print(a[i])
  
# DFS
need = [False] * (n+1)
need[n] = True

# Nから必要な子の技をたどってフラグをつけていく
for i in range(n, 0, -1):
  if not need[i]:
    continue
  for child in a[i]:
    need[child] = True
    
ans=0
for i in range(1,n+1):
  if need[i] == True:
    ans += t[i]
print(ans)
#内包表記だと早くかける
#print(sum(t[i] for i in range(1,n+1) if need[i]))