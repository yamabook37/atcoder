S = input()
n = len(S)

# 各桁の数の出現回数を求める
cnt = [[0] * 10 for _ in range(n + 1)]
for i in range(n):
    for j in range(10):
        cnt[i + 1][j] = cnt[i][j]
    cnt[i + 1][int(S[i])] += 1

# 嬉しい列を数える
ans = 0
for l in range(1, n + 1):
    for r in range(l, n + 1):
        ok = True
        for i in range(10):
            if (cnt[r][i] - cnt[l - 1][i]) % 2 == 1:
                ok = False
                break
        if ok:
            ans += 1

print(ans)
