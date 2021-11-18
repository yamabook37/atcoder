A,B=map(int,input().split())
S=input()

cnt=0
for i in range(len(S)):
  if(S[i] == "-"):
    cnt+=1
if cnt > 1:
  print("No")
  exit()

if (len(S) == A+B+1) and (S[A] == "-"):
  print("Yes")
else:
  print("No")