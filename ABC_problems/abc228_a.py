s,t,x=map(int, input().split())

# 7 20 12
if s < t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
        
# 20 7 12
# s > t
else:
    # 8時はNo, x=20(20:30)はYes, 21も
    if x < t or x >= s:
        print("Yes")
    else:
        print("No")