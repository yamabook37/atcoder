import random

n,m,k=map(int, input().split())
a=[]
ans=[0]*n
cnt=0
for i in range(k):
  i=int(input())
  a.append(i)

for i in a:
  cnt +=1

  if cnt==a[cnt] & cnt==0:
    if m>0:
      m-=1
      ans[i]+=1
    if m==0:
      ans[i]+=1
      r = random.randint(1, n)
      if r==i:
        r = random.randint(1, n)
      ans[r]-=1

  if cnt==a[cnt] & cnt>1:
    if m>0:
      m-=1
      ans[i]+=1
      r = random.randint(1, n)
      if r==i:
        r = random.randint(1, n)
      ans[r]-=1
    if m==0:
      ans[i]+=1
      r = random.randint(1, n)
      if r==i:
        r = random.randint(1, n)
      ans[r]-=1

print(ans)  

'''
3 3 4
1
1
2
3
'''