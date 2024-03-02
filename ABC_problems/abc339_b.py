#ラングトンの蟻

#方向
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

h, w, n = map(int, input().split())
s = [["." for _ in range(w)] for _ in range(h)]

direction = 0
# 0->3, 0と4が同じなので %4
pos_i = 0
pos_j = 0
#実直に実装する
for i in range(n):
    if s[pos_i][pos_j] == '.':
        s[pos_i][pos_j] = "#"
        direction += 1
    else:
        s[pos_i][pos_j] = "."
        direction += 3
    
    direction %= 4
    #あらかじめhを足して 負の値の余りを取らないように対応
    pos_i += di[direction] + h
    pos_i %= h
    pos_j += dj[direction] + w
    pos_j %= w
    
for i in range(h):
    print(*s[i], sep="")