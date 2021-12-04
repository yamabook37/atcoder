# 区間スケジューリング
# 類題ABC230 D
from operator import itemgetter

n, m = map(int, input().split())

# 区間の終端でソート
ab = sorted([tuple(map(int, input().split())) for i in range(m)], key=itemgetter(1))
# 前回除いた橋
removed = -1
ans = 0

for a, b in ab:
    # a が removed より大きい = まだ取り除いてない
    if a > removed:
        removed = b - 1
        ans += 1

print(ans)