N=int(input())
S=input()

r=S.count('R')
g=S.count('G')
b=S.count('B')
al_num=r*g*b

#全体からj-i=k-jの場合を引く
sub=0
for i in range(0,N):
  for j in range(i+1,N):
    if S[i]==S[j]:
      continue

    k = 2*j -i
    #i,j,kは等差数列なのでkは決まる, k>=Nは不適なのでスキップ
    if k>=N or S[k]==S[i] or S[k]==S[j]:
      continue
    
    sub += 1
print(al_num - sub)
# O(N^2)

'''
N=int(input())
S=input()
#print(S[1])
cnt=0

#O(N^3)だと間に合わない
for k in range(1,N+1):
  for j in range(1,k):
    for i in range(1,j):
      if (j-i)!=(k-j):
        if S[i-1]!=S[j-1] and S[i-1]!=S[k-1] and S[j-1]!=S[k-1]:
          cnt += 1
          #print(i,j,k,j-i,k-j, S[i-1],S[j-1],S[k-1])
print(cnt)


39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB
'''