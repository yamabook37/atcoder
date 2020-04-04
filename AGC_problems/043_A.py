def main():
    H, W = map(int, input().split())
    s = []
    for _ in range(H):
        S = input()
        s.append(S)
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if s[0][0] == '#' else 0 # #だと1にする
    for i in range(1, W):
        dp[0][i] = dp[0][i-1] + 1 if s[0][i] == '#' and s[0][i-1] == '.' else dp[0][i -1]
    for i in range(1, H):
        dp[i][0] = dp[i-1][0] + 1 if s[i][0] == '#' and s[i-1][0] == '.' else dp[i-1][0]
    for i in range(1, H):
        for j in range(1, W):
            if s[i][j] == '.':
                dp[i][j] = min(dp[i][j-1], dp[i-1][j])
            else:
                u = dp[i-1][j]
                r = dp[i][j-1]
                if s[i-1][j] == '.':
                    u += 1
                if s[i][j-1] == '.':
                    r += 1
                dp[i][j] = min(u, r)
    return dp[-1][-1]

print(main())