N = int(input())
B = list(map(int,input().split()))
print(B)
A = [0]*N
A[0] = B[0]
for i in range(len(A)-2):
    A[i+1] = min(B[i],B[i+1])
    
A[-1] = B[-1]  
#print(A)
print(sum(A))