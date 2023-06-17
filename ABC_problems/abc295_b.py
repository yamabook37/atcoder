R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

# 爆弾を爆発させる関数explode((r,c), power)
def explode(bomb_pos, power):
    r, c = bomb_pos
    B[r][c] = "."  # 爆弾があった場所を空きマスに変更
    #Row
    for i in range(r - power, r + power + 1):
        #Column
        for j in range(c - power, c + power + 1):
            nr, nc = i, j
            if nr >= 0 and nr < R and nc >= 0 and nc < C and not(B[nr][nc].isdigit()) and (abs(nr - r) + abs(nc - c) <= power):
                B[nr][nc] = "."  # 爆風が及ぶマスを空きマスに変更

# 爆弾があるマスを探索
for r in range(R):
    for c in range(C):
        if B[r][c].isdigit():  # 爆弾があるマスを発見
            power = int(B[r][c])  # 爆弾の威力を取得
            explode((r, c), power)  # 爆弾を爆発させる

# 爆発後の盤面を出力
for row in B:
    print("".join(row))