# 2019/09/15 300点，ぎり間に合わず 悔しい
'''
import numpy as np
def python_list_sub(in1, in2):
    wrk = np.array(in1) + np.array(in2)
    return wrk.tolist()
'''

n, k, q = map(int,input().split())
Po = []
#De = [1 for i in range(n)]

A = [int(input()) for i in range(q)]
#print(A)

# はじめからポイント減らしておく:ここが味噌
for i in range(n):
    Po.append(int(k-q))
#print(Po)
# 入力OK

#計算，正解者だけ足していく
for j in A:
    #print(j,A[j])
    Po[j-1] += 1
#print(Po)

for i in range(n):
    if Po[i] >0:
        print('Yes')
    else: print('No')