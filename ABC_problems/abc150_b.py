N=int(input())
s=input()
S=list(s) #全て入れたのち文字列をリストに変換する
#print(S[0])
flg=0
for i in range(N-2): #末尾によってはここが反応してしまう
    if S[i] == 'A':
        if S[i+1] =='B':
            if S[i+2] =='C':
                flg+=1
print(flg)

'''
10
ZABCDBABCQ

19
THREEONEFOURONEFIVE

33
ABCCABCBABCCABACBCBBABCBCBCBCABCB
'''