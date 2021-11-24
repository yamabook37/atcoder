a,b,c = map(int, input().split())
num = a+b+c
if num <= 21:
    print("win")
else:
    print("bust")