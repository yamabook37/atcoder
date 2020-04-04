s = input()

prev = ""
lets = ""
ans = 0
for i in s:
  lets += i
  if lets != prev:
    ans += 1
    prev = lets
    lets = ""

print(ans)