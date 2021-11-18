from itertools import accumulate

def my_prime(n):
    if n==1:
        return 0
    for k in range(2, int(n**0.5)+1 ): #検索範囲注意
        if n%k ==0:
            return 0
    return 1


Q = int(input())
L = [0]*Q
R = [0]*Q

for i in range(Q):
    L[i], R[i] = list(map(int, input().split()))

min_L = min(L)
max_R = max(R)

ans=[]
for i in range(min_L, max_R +1):
    if i%2 == 1:
        flg = (my_prime(i) and my_prime((i+1)/2) )
    else:
        flg = 0
    ans.append(flg)

# ここに累積和
ans = [0] + ans
ans = list(accumulate(ans))

for i in range(Q):
    print(ans[R[i] - min_L + 1] - ans[L[i] - min_L])



