# traveling
n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    # x+y > t　No
    # x+y とtの偶奇が違うならNo
    # ここを思いつけば勝ち！
    if ((x+y) > t) or ((x+y +t)%2):
        print("No")
        exit()
print("Yes")
