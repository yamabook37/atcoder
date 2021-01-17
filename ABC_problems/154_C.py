n = int(input())
a = input().split()
# 同じものを除外
b = set(a)
if len(a) == len(b):
    print("YES")
else:
    print("NO")
