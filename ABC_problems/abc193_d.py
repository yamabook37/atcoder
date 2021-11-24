K = int(input())
S = input()[:4]
T = input()[:4]
# 末尾1文字は#, 頭から4つを取得

# 解説
'''
まだ見えていない 9K−8 枚をそれぞれ区別して考える
(高橋くんの勝つ確率) = (高橋くんの勝つ配り方の数) / (全ての配り方の数)
高橋くんの勝つ配り方の数は、高橋くんの勝つような (x,y) の組についてこの総和を取れば求められる
'''

cnt = [K] * 10
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1
#print(cnt)

def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans

ans = 0

# x!=y
for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(S + str(i)) > score(T + str(j)):
            ans += cnt[i] * cnt[j]

# x=y
for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(S + str(i)) > score(T + str(i)):
        ans += cnt[i] * (cnt[i] - 1)

N = 9 * K - 8
print(ans / N / (N - 1))
