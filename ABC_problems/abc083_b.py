N,A,B=map(int,input().split())

ans = 0
for i in range(N+1):
  #文字列に変換
  num = list(str(i))
  #mapでint型に結合
  keta = list(map(int, num))
  #print(sum(keta))
  if A <= sum(keta) <= B:
    ans += i
print(ans)