#ABC_161_C
N,K=map(int,input().split())
A=[]

if K==1 or N%K==0:
  print(0)
  exit()

tmp=N%K
#print(tmp)
ans=abs(tmp-K)
print(min(tmp,ans))