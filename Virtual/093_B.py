# 15min
A,B,K=map(int,input().split())
ans=[]
for i in range(K):
  if A+i <= B:
    ans.append(A+i)
  if B-i >= A:
    ans.append(B-i)

for i in sorted(set(ans)):
  print(i)