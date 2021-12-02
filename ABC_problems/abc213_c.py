# H 行 W 列
H, W, N = map(int, input().split())
A = []
B = []

for _ in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

As = sorted(set(A))  # `set`で重複を省いてソートしたリスト
Bs = sorted(set(B))

# 行、列は対称
# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じ
Ad = {x: i for i, x in enumerate(As, 1)}
Bd = {x: i for i, x in enumerate(Bs, 1)}

for a, b in zip(A, B):
  print(Ad[a], Bd[b])

'''
行と列の操作はお互いに関係がないので、行と列で 2回同じことをする

カードの行番号のリストRを受け取る
Rから重複を省いて、小さい順にソートしたリストRsを用意する
Rsをつかって、元の行番号が上から何番目に対応するかの辞書Rdを作る
なお、これは『座標圧縮』と呼ばれるテクニック
'''