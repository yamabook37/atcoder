A=int(input())
B=int(input())
C=int(input())
X=int(input())
cnt=0

# 全探索
for i in range(A+1):
  for j in range(B+1):
    for k in range(C+1):
      tmp = 500*i + 100*j + 50*k
      if tmp==X:
        cnt+=1
print(cnt)