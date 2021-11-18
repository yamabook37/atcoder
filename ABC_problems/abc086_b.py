a,b=input().split()
ans=int(a+b)
for i in range(1000):
  if i*i == ans:
    print("Yes")
    exit()
print('No')