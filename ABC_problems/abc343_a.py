a,b=map(int, input().split())
ans=a+b
num=[0,1,2,3,4,5,6,7,8,9]

if ans == 0:
    print(ans+1)
    exit()
if ans == 9:
    print(ans-1)
    exit()
else:
    print(ans+1)
    exit()
