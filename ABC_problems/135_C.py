N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    if A[i] >= B[i]:
        ans += B[i]
    elif A[i]+A[i+1] > B[i]:
        ans += B[i]
        A[i+1] = A[i]+A[i+1] -B[i] #残り
    else: #B[i]が大きいとき，A[i+1]を消費済みにする
        ans += A[i]+A[i+1]
        A[i+1] = 0
print(ans)

# 理解した
