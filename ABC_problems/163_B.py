N,M=map(int,input().split())
A= [int(i) for i in input().split()]
if sum(A) >N:
  print('-1')
  exit()
#print(sum(A))
print(N-sum(A))