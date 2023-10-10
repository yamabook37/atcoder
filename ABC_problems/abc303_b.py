n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for _ in range(m)]

# 人数分の友達フラグ 2次元
friend_flg = [[False] * n for _ in range(n)]
#print(friend_flg)

for photo in a:
    for i in range(n - 1):
        # TODO:重複x,y y,xを2で割る
        friend_flg[photo[i] - 1][photo[i + 1] - 1] = True
        friend_flg[photo[i + 1] - 1][photo[i] - 1] = True

cnt = 0
for person in friend_flg:
    # -1: 自分自身
    cnt += person.count(False) - 1
print(cnt // 2)