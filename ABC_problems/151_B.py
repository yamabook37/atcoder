n,k,m=map(int, input().split())
a=[int(i) for i in input().split()]
#print(a)
su=0
for i in range(n-1):
    su+=a[i]

ans=n*m-su
if ans<=0:
    print(0)
elif ans>k: #kはセーフやん
    print(-1)
else:
    print(ans)