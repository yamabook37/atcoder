H,W=map(int,input().split())
R,C=map(int,input().split())

ans=0
# 左側にマスがある
if C != 1:
    ans+=1
# 右側にマスがある
if C != W:
    ans+=1
# 上側にマスがある
if R != 1:
    ans+=1
# 下側にマスがある
if R != H:
    ans+=1
print(ans)

