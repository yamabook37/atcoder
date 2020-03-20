# 2020/03/17, 4min 15:46
r, D, x = map(int,input().split())
ans=[x]
for i in range(10):  
  tmp = r*ans[i] - D
  ans.append(tmp)
  print(tmp)