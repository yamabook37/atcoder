N, D = map(int, input().split())
day = [[] for _ in range(D)]
#print(day)

for i in range(N):
    S = input()
    for j in range(D):
        day[j].append(S[j])
#print(day)

all_free = ["o" for _ in range(N)]
#print(all_free)

ans = 0
con = 0 #何日連続するか
for i in range(D):
    if day[i] == all_free:
        con += 1
    else:
        ans = max(ans, con)
        con = 0
ans = max(ans, con)
print(ans)