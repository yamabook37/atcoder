N,K=map(int,input().split())
ans=[]
A=[]
for i in range(K):
  d=int(input())
  A= input().split()
  ans=ans+A

#print(ans)
l=set(ans)
#print(l)
print(N-len(l))