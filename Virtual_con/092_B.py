N=int(input())
D,X=map(int,input().split())
A=[]
for i in range(N):
  inp = int(input())
  A.append(inp)
#print(A)
for i in range(N):
  X+=1
  X+=(D-1)//A[i]
print(X)