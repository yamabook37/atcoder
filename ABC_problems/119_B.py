# 2020/03/18, 12min 23:22-20:34
N=int(input())
Num = []
Alp = []
# 複数行に数値と文字列を格納，まとめて受けて，それぞれリストへ入れる
for i in range(N):
    n, a = input().split()
    Num.append(float(n))
    Alp.append(a)
#print(Num)

ans=jp=bt = 0
for i in range(N):
  if Alp[i]=='JPY':
    jp += Num[i]
  if Alp[i]=='BTC':
    bt += Num[i] * 380000.0
ans = jp + bt
print(ans)
