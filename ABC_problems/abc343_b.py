n=int(input())
pair = [tuple(map(int, input().split(' '))) for i in range(n)]
# print(pair)
#1があるindex+1を出力

ans = []
zero_flg = 1
for i in range(n):
    ans = []
    for j in range(n):
        if pair[i][j] == 1:
            zero_flg = 0
            #print(j+1)
            ans.append(j+1) 
    if zero_flg == 0:
        print(*ans, sep=" ")
    else:
        print()
