N,K=map(int,input().split())
A=list(map(int,input().split()))
ans=list()

#print(A)
for i in range(K):
    A.pop(0)
    A.append(int("0"))
print(*A)