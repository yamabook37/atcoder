# 面白そう
A,B,C = map(float,input().split())
lim = 100.0
ans = 0

ans = (lim-A)*(A/(A+B+C)) + (lim-B)*(B/(A+B+C)) + (lim-C)*(C/(A+B+C))
print(ans)