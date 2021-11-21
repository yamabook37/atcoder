N = int(input())

node = [0] * N
for _ in range(N-1):
  a, b = list(map(int, input().split()))

  # 各ノードから出る辺の数をカウント
  node[a-1] += 1
  node[b-1] += 1

# スター：中心(最も連結が多い頂点)からの葉の数がN-1
if max(node) == N-1:
  print("Yes")
  exit()

print("No")