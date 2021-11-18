N = int(input())
S = list(input())
ans = 0
for i in range(N):
  A = S[:i]
  B = S[i:]
  C = list(set(A) & set(B))
  #print(C)
  c = len(C)
  if c > ans:
    ans += 1

print(ans)
