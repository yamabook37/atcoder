from collections import defaultdict

c2idx = {c: i for i, c in enumerate("KEY")}
S = list(map(lambda x: c2idx[x], input()))
K = int(input())

cnts = [[[0, 0, 0]] for _ in range(3)] # 1-idxed
cnt = [0, 0, 0]
for s in S:
  cnt[s] += 1
  cnts[s].append(tuple(cnt))
final_cnt = cnt

# 連想配列DP
dp = defaultdict(int) # (交差数node, *cnt) -> 種類の数
dp[0, 0, 0, 0] = 1
for _ in range(len(S)):
  dp_new = defaultdict(int)
  for (node, *cnt), n in dp.items():
    for i in range(3):
      if cnt[i]+1<=final_cnt[i]:
        cnt_ = list(cnt)
        cnt_[i] += 1
        node_ = node + sum([max(0, c1-c2) for c1, c2 in zip(cnt_, cnts[i][cnt_[i]])])
        dp_new[node_, cnt_[0], cnt_[1], cnt_[2]] += n
  dp = dp_new
  
ans = 0
for (node, *cnt), n in dp.items():
  ans += (node <= K)*n
print(ans)
