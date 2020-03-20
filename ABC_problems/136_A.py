a,b,c=map(int,input().split())
ans=b+c-a
if ans<0:
  print(0)
  exit()
print(ans)