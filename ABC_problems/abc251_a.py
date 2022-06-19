S=input()
l=len(S)
rep=int(6/l)
ans=''

for i in range(rep):
    ans+=S
print(ans, end='')