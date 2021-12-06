# 再帰DFS, Python3.8で提出

def main():
  import sys
  sys.setrecursionlimit(10 ** 6)  
  # 最大で再帰の深さが2 * 10 ** 5程度になるので、それ以上に設定

  # 木上のDFSなので、どの頂点から来たかを引数pで渡せば、訪問済みの頂点を覚えなくても済む
  def dfs(u, p):
    ans.append(u)  # はじめて訪問したとき
    for v in edge[u]:
      if v != p:
        dfs(v, u)
        ans.append(u)  # 他の頂点に行って帰ってくるたび

  N = int(input())
  edge = [[] for _ in range(N + 1)]
  for i in range(N - 1):
    a, b = map(int, input().split())
    # 
    edge[a].append(b)
    edge[b].append(a)

  # 小さい順にsortを忘れるとWA
  for i in range(N + 1):
    edge[i].sort()

  ans = []
  dfs(1, -1)
  print(*ans)


if __name__ == '__main__':
  main()