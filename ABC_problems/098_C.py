from itertools import accumulate

N = int(input())
S = list(input())

A = [0]*(N+1) #N+1まで入れること忘れず

#リーダーの方向を向く，W->1の累積和，[0]start
for i in range(1, N+1):
    j = 0
    if S[i-1] == "W":
        j = 1
    A[i]=A[i-1] +j
#A =list(accumulate(A))
#print(A)

#iより左にいて西を向いている人の最小値
ans=N
for i in range(1, N+1):
    val = N-i +A[i] -A[N]
    ans = min(ans, A[i-1] +val)

print(ans)

'''
5
WEEWW

12
WEWEWEEEWWWE
'''