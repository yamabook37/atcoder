seen: その頂点を検知済みかどうかを表す配列
todo: 検知したがまだ訪問済みでない頂点の集合 (保留中の頂点の集合)

### アルゴリズム
seen 全体を false に初期化して、todo を空にする
seen[s] = true として、todo に s を追加する
todo が空になるまで以下を繰り返す:
todo から一つ頂点を取り出して v とする
T(v) の各要素 w に対して、
  seen[w] = true であったならば、何もしない
  そうでなかったら、seen[w] = true として、todo に w を追加する

## 深さ優先探索 DFS Depth First Search
スタック
LIFO (Last-In First-Out) 

## 幅優先探索 BFS
キュー
FIFO (First-In-First-Out)
# 今回は扱わない

### DFSの特徴
グラフの場合、一筆書きで回ることができる
いった順に頂点を回収：行きがけ順
最後に行った頂点から回収：帰りがけ順
