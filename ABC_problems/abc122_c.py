from itertools import accumulate

N, Q = map(int, input().split())
S = input()
A = [list(map(int, input().split())) for i in range(Q)]
# リストに入れておく
#print(A)

flg = []
for i in range(N-1):
    tmp_S = S[i:i+2]
    if tmp_S == 'AC':
        flg.append(1)
    else:
        flg.append(0)
# print(len(flg)) #N-1になっていることを確認

ans = []
ans = [0] + flg #繋げて
ans = list(accumulate(ans)) #累積和にする
#print(ans)

for li in A:
    print(ans[li[1]-1] - ans[li[0]-1] )

'''
8 3
ACACTACG
3 7
2 3
1 8
'''