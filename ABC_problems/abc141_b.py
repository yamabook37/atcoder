#2019/09/15 正解200
s = input()
inp = list(s)

L_o = ['R','U','D']
L_e = ['L','U','D']
c = 0
l = len(s)

for i in range(l): #文字数だけループ
    if i%2 ==0 : #偶数
        for j in range(l):
            if 'L' in inp[i]: #Rを検索
                print('No')
                exit() 
    elif i%2 ==1: #奇数
        for k in range(3):
            if 'R' in inp[i]:
                print('No')
                exit()
print('Yes')