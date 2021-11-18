# 2020/03/17, 9min
N,X = map(int,input().split())
L = [int(i) for i in input().split()]
#print(L)
cnt=0
D = [0]
for i in range(N):
  tmp = D[i]+L[i]
  D.append(tmp)
  if tmp <= X:
    cnt += 1
print(cnt+1)
#初期値の0を追加