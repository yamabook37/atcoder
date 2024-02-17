from itertools import accumulate

# Kこの連続する整数の和の最大値

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 累積和
B = [0] + A
B = list(accumulate(B))

ans = []
for i in range(N-K):
    ans.append(B[i+K]-B[i])
    # 記事主https://upura.hatenablog.com/entry/2019/04/01/212701
    # Kとするべきを3としている

print(max(ans))