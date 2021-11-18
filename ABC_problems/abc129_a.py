P,Q,R=map(int,input().split())
ans=[]
ans.append(P)
ans.append(Q)
ans.append(R)

sorted(ans)
print(P+Q+R-max(ans))