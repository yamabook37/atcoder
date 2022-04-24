import math

x,y=map(int,input().split())
diff=y-x
if diff <= 0:
    print('0')
else:
    ans=math.ceil(diff / 10)
    print(ans)