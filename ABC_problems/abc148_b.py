N=int(input())
S,T = input().split()
#print(list(S))
Sl = list(S)
Tl = list(T)
ans=[]

for i in range(N):
    ans.append(Sl[i])
    ans.append(Tl[i])
ans=''.join(ans)
print(ans)

'''
hmhmnknk uuuuuuuu
'''