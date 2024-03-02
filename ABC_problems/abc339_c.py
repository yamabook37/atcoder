INF = (1 << 60)

N=int(input())
A=list(map(int, input().split()))

min_A=INF
ans=0
for i in range(N):
    ans += A[i]
    # 累積和ansの最小値min_A
    min_A = min(min_A, ans)

initial=0
if min_A < 0:
# 累積和の最小値が負の値であれば、それを0にするように乗客を乗せる
    initial = -(min_A)
    # min_Aは負なので-かけて正にする
print(initial + ans)