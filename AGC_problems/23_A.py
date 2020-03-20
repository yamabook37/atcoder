from itertools import accumulate
import collections

n = int(input())
A = list(map(int,input().split()))
#print(A)

#累積和
B = [0] + A
B = list(accumulate(B))

num = collections.Counter(B)
# counterオブジェクトを返す
cm = num.most_common()
#登場回数順にカウント，(要素，出現回数)を昇順でリストにして返す
# どの数字が何個あるかカウント
#print(cm)

# 集計
ans = 0
for li in cm:
    #print(li[1])
    if li[1]>1: #2回出たやつのみカウント=同じになる区間(足して0のこと)があると言うこと ,li[1]は出現回数
        ans += (li[1] * (li[1]-1) //2) # xC2 を計算=値の同じ二個の要素の選ぶ方法の数=答え
print(ans)