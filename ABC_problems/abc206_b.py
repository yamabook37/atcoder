N = int(input())

ans = 0
cnt = 0
while(1):
  cnt += 1
  ans += cnt
  if ans >= N:
    print(cnt)
    exit()