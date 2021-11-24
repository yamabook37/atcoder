'''
N個から2個選ぶ場合の数
NC2= N(N-1)//2

Ai=Aj となる補集合を考えて引く
Ai の値を数値ごとに分類して、その個数をaとして aC2 の総和を取っていけば OK

参考
https://note.nkmk.me/python-collections-counter/
'''

from collections import Counter
N=int(input())
A=[int(i) for i in input().split()]

#Aの分類と数え上げ, 要素をカウント
c = Counter(A)
#print(c)

# aC2の総和:補集合
cnt = 0
for i in c.keys():
  cnt += c[i] * (c[i] - 1) // 2
  #print(cnt)

# 全通り-補集合でAi!=Aj
print(N*(N-1)//2 - cnt)