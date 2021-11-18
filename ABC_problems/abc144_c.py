# coding: utf-8

# 整数 > 整数型
def I(): return int(input())

# 整数列 '1 2 3 4' > 整数型リスト
def IsIl(): return list(map(lambda x: int(x), input().split()))

# 改行挟む整数列　'1/n 2/n 3/n' > 整数型りすと
def InIl(n): return [input() for i in range(n)]

# 整数列 '1 2' > 整数型タプル
def IsIt(): return map(lambda x: int(x), input().split())

# 改行挟む整数列　'1\n 2\n 3\n' > 整数型たぷる
def InIl(n): return map(input() for i in range(n))

# 文字列 'abcd' > 文字型リスト
def SsSl(): return list(map(lambda x: x, input()))

# 整数 '1234' > 整数型リスト

# 文字列 'aba' > 辞書（文字型:個数）{'a':2,'b':1}
def SSd():
    from collections import defaultdict
    A = input() # [int(i) for i in input().split()]
    dd=defaultdict(int)
    for a in A:
        dd[a]+=1
    return dd


import math

n=I()
#n<=10^12
nmax = int(n**0.5)
#print(nmax)
for i in reversed(range(nmax)):
    if n%(i+1) == 0: #大きい方の約数=i+1
        #print(i)
        print(int(n/(i+1)) + (i-1))
        break
