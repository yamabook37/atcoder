N = int(input())
# N行の入力をリストに入れる
D = [list(map(int, input().split())) for i in range(N)]
Q = int(input())
# こっちは1この整数をQ行
P = [int(input()) for i in range(Q)]

# 2次元累積和
S = [[0 for i in range(N+1)] for j in range(N+1)]
    # 全ての要素0の2次元リスト
#print(S)
for i in range(N):
    for j in range(N):
        # 長方形区間のお絵かきより
        S[i+1][j+1] = S[i][j+1] + S[i+1][j] - S[i][j] + D[i][j]

val = [0]*(N*N+1)   # val[v] := 面積が v の長方形領域の総和の最大値
for x1 in range(0, N):
    for x2 in range(x1+1, N+1):
        for y1 in range(0, N):
            for y2 in range(y1+1, N+1):
                area = (x2-x1)*(y2-y1)
                v = S[x2][y2] - S[x1][y2] - S[x2][y1] + S[x1][y1]
                val[area] = max(val[area], v)
                # 最大値を更新していく

# val[v] := 面積が v 「以下」の長方形領域の総和の最大値
for i in range(0, N*N):
    val[i+1] = max(val[i+1], val[i])

for p in P:
    print(val[p])