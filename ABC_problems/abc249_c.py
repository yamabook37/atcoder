'''
入力例
4 2
abi
aef
bc
acg
'''

# 解法：選んだ文字列の中でちょうど K 個の文字列に登場する英小文字」の種類数を求めて最大値を出力
import itertools
import collections

n, k = map(int, input().split())
S = [] #ここにS0,S1,...,Snを入れていく 

for i in range(n):
    s = list(input()) #collections.Counterを使いたいので、入力をリストにしておく
    S.append(s)

#S = [['a', 'b', 'i'], ['a', 'e', 'f'], ['b', 'c'], ['a', 'c', 'g']]

comb = [] #ここに0~n-1の中から、1~n個選ぶ時の組み合わせを入れていく

for i in range(1, n+1):
    comb += list(itertools.combinations(range(n), i))

#comb = [(0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

ans = 0

for c in comb:
    cnt = 0
    L = []
    for cc in c:
        L += S[cc]
    #例えば、c = (0, 1) の時、Lの中身はこんな感じ。選んだsを全部繋げている。
    #L = ['a', 'b', 'i', 'a', 'e', 'f']
    dic = collections.Counter(L)
    #collection.Counter()は、リストの要素をkey, 要素の出現回数をvalueにもつディクショナリ。中身はこんな感じ
    #dic = Counter({'a': 2, 'b': 1, 'i': 1, 'e': 1, 'f': 1})
    for d in dic:
        #出現回数がkのものがあったらcntに1足す
        if dic[d] == k:
            cnt += 1
    #最大値を更新したら置き換える
    if cnt>ans:
        ans = cnt

print(ans)