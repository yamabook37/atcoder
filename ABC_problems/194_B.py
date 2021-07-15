N = int(input())
A = [0]*N
B = [0]*N
A_cnt = 0
B_cnt = 0
res = float('inf')

for i in range(N):
  A[i],B[i] = map(int, input().split())

#2重ループで全探索
for i in range(N):
  for j in range(N):
    res = min(res, A[i]+B[j] if i==j else max(A[i],B[j]))
print(res)

'''
x_min = x[0]
y_min = y[0]

for i in range(N):
  if x[i] < x_min:
    x_min = x[i]
    x_cnt = i
  if y[i] < y_min:
    y_min = y[i]
    y_cnt = i
print(x_min, y_min, x_cnt, y_cnt)

if x_cnt == y_cnt:
  ans_a = x_min + y_min
else:
  ans_a = max(x_min, y_min)
'''


'''
3
8 5
4 4
7 9
'''
