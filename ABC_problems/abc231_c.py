N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]

# クエリの入力
X=[]
for i in range(Q):
  x=int(input())
  X.append((x,i))
# クエリもソートできる, AとXをまとめてソート
# 範囲を全指定にしてマイナスステップにすると、要素がリバース
AX=sorted(A+X)[::-1]
#print(AX)

ans=[0]*Q
cnt=0
for x,i in AX:
  if i<Q:
    ans[i]=cnt
  else:
    cnt+=1
# ansリストをアンパック
print(*ans,sep="\n")




'''
# TLE
N,Q=map(int,input().split())
A=list(map(int, input().split()))

S=[]
S=sorted(A, reverse=True)
#print(A,S)

for j in range(1,Q+1):
  x=int(input())
  ans = 0
  
  for i in range(len(S)):
    if x > S[i]:
      #print('if',x,S[i])
      break
    elif x <= S[i]:
      ans += 1
  
  print(ans)
'''

'''
5 5
1 2 3 4 5
6
5
4
3
2
'''