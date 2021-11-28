# bit全探索
# https://drken1215.hatenablog.com/entry/2019/12/14/171657

# この機会にしっかり勉強する

N = input()

K = len(N)

ans = 10 ** 10
for i in range(1, 2 ** K):
    pattern = [0] * K
    for j in range(K):
        if (i >> j) & 1:
            pattern[j] = 1

    temp = 0
    for p, q in zip(pattern, N):
        temp += p * int(q)
    if temp % 3 == 0:
        ans = min(ans, K - sum(pattern))

print(ans if ans != 10 ** 10 else -1)