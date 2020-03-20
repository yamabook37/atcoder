# 2020/03/17, 18min, 15:55-16:13
N = int(input())
W = [int(i) for i in input().split()]
# ある整数T(N-1) ，以下か以上かで区切ったときも，全て考える必要あり
ans = 1000
for i in range(1, N):
    tmp = abs(sum(W[:i]) - sum(W[i:]))
    # スライスで区切って和をとる，最小値を更新していく
    # :i 初めからiまで
    if ans > tmp:
        ans = tmp
print(ans)

'''
8
27 23 76 2 3 5 62 52
'''