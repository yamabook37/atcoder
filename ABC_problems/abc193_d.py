K = int(input())
S = input()[:4]
T = input()[:4]
# 末尾1文字は#, 頭から4つを取得

# 解説
'''
まだ見えていない 9K−8 枚をそれぞれ区別して考える
  すなわち最後の一枚の81通りを区別して考える 等しいor等しくない場合
(高橋くんの勝つ確率) = (高橋くんの勝つ配り方の数) / (全ての配り方の数)
高橋くんの勝つ配り方の数は、高橋くんの勝つような (x,y) の組についてこの総和を取れば求められる

6
1122#
2228#

1,1,2,2, 2,2,2,8を使用
残り1*4, 2*1, 3,4,5,6,7,9*6, 8*5 Total46枚
S に入るカードを選ぶ方法が 46 通り (一般には 9K−8 通り)
T に入るカードを残りのカードから選ぶ方法が 45 通り (一般には 9K−9 通り)
46*45 = 2070
最後が2:1通り or 1:2通り
よって2/2070=1/1035

参考
けんちょんさん
https://drken1215.hatenablog.com/entry/2021/03/02/190700
ヤマカサさん
https://yamakasa.net/atcoder-abc-193-d/
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
