N = int(input())

cnt = 0
ans = -1
ans_list = []

for i in range(N):
  A, P, X = map(int, input().split())
  if X-A > 0:
    cnt += 1
    ans_list.append(P)

if cnt == 0:
  print(-1)
  exit()

print(min(ans_list))