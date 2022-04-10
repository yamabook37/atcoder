N = int(input())

ss = []
ts = []
#入力処理
for _ in range(N):
    s, t = input().split()
    ss.append(s)
    ts.append(t)

a_exist = []

for i in range(N):
#1,2,...,N
    nickname_ok = False
    for a in [ss[i], ts[i]]:
        for j in range(N):
            if i == j:
                continue

            #同じ名前、苗字がいればフラグ
            if a == ss[j] or a == ts[j]:
                nickname_ok = False
                break
        else:
            nickname_ok = True
            break
    if not nickname_ok:
        print('No')
        break
else:
    print('Yes')

'''
3
tanaka taro
tanaka jiro
suzuki hanako
'''