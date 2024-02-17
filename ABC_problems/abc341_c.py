def count_possible_positions(H, W, S, T):
    ans=0
    I=J=0

    #高橋君の移動経路上のマス（不時着したマスおよび現在いるマスを含む）はいずれも海でない
    #そのマスに不時着したとするとそこから海に入らずにT に従う移動ができるか
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == '#':
                continue
            ok_flg = True
            I = i
            J = j
            
            for move in T:
                if move == 'L':
                    J -= 1
                elif move == 'R':
                    J += 1
                elif move == 'U':
                    I -= 1
                elif move == 'D':
                    I += 1
                    
                #Tを実行して海にはいないことが保証されている, 陸'.'にいればok -> カウント
                if S[I][J] == '#':
                    ok_flg = False
                    break
            if ok_flg:
                ans += 1
    return ans

H, W ,N= map(int, input().split())
T = input()
# print(T[0])
S = [input() for _ in range(H)]
print(count_possible_positions(H, W, S, T))