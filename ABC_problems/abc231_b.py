from collections import Counter

N=int(input())
A=[]*N

for i in range(N):
  S=input()
  A.append(S)
Set=set(A)
#print(A, Set)

C=[]
C=Counter(A)
keys, values = zip(*C.most_common())
#print(keys,values) 
print(keys[0])