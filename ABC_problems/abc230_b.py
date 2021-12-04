S=input()
num = len(S)
T='oxx' * (num//3 +2)
#print(S,T)
if S in T:
  print('Yes')
else:
  print('No')

'''
#oの次にx,xが来ないとダメ
for i in S:
  if S[i]=='o' & S[i+1]=='x' & S[i+2]=='x':
'''

