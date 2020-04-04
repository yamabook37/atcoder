N,M=map(int,input().split())
a=[[int(b) for b in input().split()] for i in range(N)]
c=[[int(d) for d in input().split()] for i in range(M)]
for i in range(N):
  p=a[i]
  tmp=10**10 #ここ小さいとWAになる
  pos=-1
  for j in range(M):
    cp=c[j]
    dist=abs(cp[0]-p[0])+abs(cp[1]-p[1])
    if dist < tmp:
      tmp=dist
      pos=j+1
      #print(pos)
  print(pos)
