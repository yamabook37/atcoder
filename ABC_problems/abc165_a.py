import math
K=int(input())
A,B=map(int, input().split())

for i in range(1,1020):
  if K*i >= A and K*i <= B:
    print('OK')
    #print(K*(c+i))
    exit()
  i+=1
print('NG')

