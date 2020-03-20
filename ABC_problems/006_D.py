# 秘伝のたれ　もらっておこう

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

# これは何ソートだ？
def lis(li):
    lis_li = [li[0]]
    for i in li:
        if i > lis_li[-1]:
            lis_li.append(i)
        else:
            lis_li[bisect_left(lis_li, i)] = i
            # bisect ライブラリとはなんぞや
    return lis_li
 
 
n = I()
# 枚数nの入力
print(n - len(lis(IR(n))))