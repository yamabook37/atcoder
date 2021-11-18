H, W, K = map(int, input().split())
#Ci,jを表す配列を作成する
c = []
for i in range(H):
    c.append(input())

ans = 0

# 各行のYes or Noに関して列のYes or Noの全通りを試す
# bit演算を行うことで全通りを簡単に試すことができる
for h in range((1 << H)):
    for w in range((1 << W)):
        black = 0
        # 各行の各列
        for i in range(H):
            for j in range(W):
                if ((h >> i) & 1) == 0 and ((w >> j) & 1) == 0 and c[i][j] == '#':
                    black += 1
        if black == K:
            ans += 1

print(ans)
