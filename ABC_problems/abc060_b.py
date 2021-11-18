A,B,C=map(int, input().split())
ans=[]
i = 1
while 1:
  x = A * i
  mod = x % B
  if mod == C:
    print("YES")
    exit()
  if mod in ans:
    print("NO")
    exit()
  ans.append(mod)
  i+=1