# お年玉
# easy 09/15
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce
 
 
INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

#この秘伝のタレは正直微妙？

n, y = map(int, input().split())
# yは1000の倍数
for i in range(n + 1):
    for j in range(n -i +1): #1枚目の種類を決める
        if i*10000 + j*5000 + (n-i-j)*1000 == y:
        # 3種類目は自動で決まる(n-1枚目-2枚目)のがみそ、これでfor2回でいける
            print(i, j, n-i-j)
            #正解例は複数あるが初めに見つかったもので出力して良い
            exit()
# 例外はループの外
print("-1 -1 -1")