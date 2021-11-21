A=[int(b) for b in input().split()]
B=A[:]
A[0]=B[2]
A[1]=B[0]
A[2]=B[1]
print(A[0], A[1], A[2])