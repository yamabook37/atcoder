N = int(input())
P = [int(i) for i in input().split()]

cnt = 0
for i in range(N):
    if P[i] != i + 1:
        cnt += 1
if cnt > 2:
    print('NO')
else:
    print('YES')
