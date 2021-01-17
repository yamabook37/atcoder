N=int(input())
ans=[]
cnt=0
for i in range(1,N+1):
  if i%15!=0:
    if i%5!=0:
      if i%3!=0:
        ans.append(i)
  #print(ans)
print(sum(ans))
