'''
制約1<=N<=10^10 全探索では間に合わない
反対に a**b と表せる整数をすべて列挙して、その個数を NN から引く
'''

N = int(input())

# a ** b の形で表せる数, 2**4=4**2などの重複を省く
# Listでは遅いのでset型の集合を使用
S = set()  

# sqrt(N)**2 > N より、(10 ** 5 + 1)**2 > 10**10 なので、10**5まで(sqrt(N))調べればいい
for a in range(2, 10 ** 5 + 1):
  val = a ** 2  # a ** 2 から
  # 内側はN
  while val <= N:
    S.add(val)
    # add() 要素を追加, remove() 削除, clear() 空にする
    val *= a
#補集合：a**bと表せるもの
#print(S)

print(N - len(S))
