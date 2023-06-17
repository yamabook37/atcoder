# DFS: stackによる実装, 後入れ先出し LIFO (Last-In First-Out) 
# 再帰のものより早い

# https://qiita.com/takayg1/items/7008e4c9584e42ae13c7
# 入力
# 1行目に頂点の個数を整数で、その後N行に頂点番号、隣接する頂点の個数、隣接する頂点を空白区切りで入力
'''
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0
'''
# 出力
# N行に、頂点番号、到達時刻、探索終了時刻が空白区切りで出力（行きがけ順では前者のみ、帰りがけ順では後者のみ）
'''
1 1 12
2 2 11
3 3 8
4 9 10
5 4 7
6 5 6
'''


# 深さ優先探索（行きがけ）
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
  u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
  v.sort()
  for i in v:
    graph[u].append(i)
    # graph[i].append(u) # 無向グラフ

time = 0
arrive_time = [-1] * (N + 1) # 到着時刻

# 深さ優先探索
def dfs(v):
  global time
  time += 1
  stack = [v]
  arrive_time[v] = time
  while stack:
    v = stack[-1]
    if graph[v]:
      w = graph[v].popleft()
      if arrive_time[w] < 0:
          time += 1
          arrive_time[w] = time
          stack.append(w) 
    else:
      stack.pop()          
  return arrive_time

# 孤立している頂点対策
for i in range(N):
  if arrive_time[i + 1] < 0:
    ans = dfs(i + 1)

# 頂点番号、到着時刻
for j in range(N):
  temp = [j + 1, ans[j + 1]]
  print(* temp)





# 深さ優先探索（帰りがけ）
from collections import deque

# グラフの作成(無向グラフでは#を消す)
N = int(input())
graph = [deque([]) for _ in range(N + 1)]
for _ in range(N):
  u, k, * v = [int(x) for x in input().split()] # uは頂点番号、kは隣接頂点の個数
  v.sort()
  for i in v:
    graph[u].append(i)
    # graph[i].append(u) # 無向グラフ

time = 0
arrive = [-1] * (N + 1) # 到着したか
finish_time = [-1] * (N + 1) # 探索終了時刻

# 深さ優先探索
def dfs(v):
  global time
  stack = [v]
  arrive[v] = 1
  while stack:
    v = stack[-1]
    if graph[v]:
      w = graph[v].popleft()
      if arrive[w] < 0:
        arrive[w] = 1
        stack.append(w) 

    else:
      time += 1
      finish_time[v] = time
      stack.pop()          
  return finish_time

# 孤立している頂点対策
for i in range(N):
  if arrive[i + 1] < 0:
    ans = dfs(i + 1)

# 頂点番号、終了時刻
for j in range(N):
  temp = [j + 1, ans[j + 1]]
  print(* temp)