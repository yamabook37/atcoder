# 20min
X=int(input())
x=0
ans=[]

if X == 1:
  print(X)
  exit()
else:
  # p
  for i in range(2, int(X**0.5)+1):
    n=1
    a=i
    # b
    while n < X : #超えたら中断
      n *= a
      ans.append(n)
    if n // a > x:
      x = (n//a)
      #print(ans)
  print(max(i for i in ans if i <= X))