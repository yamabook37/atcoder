n=int(input())
s=list(input())
#print(s)
flg_a=0
flg_b=0
flg_c=0
for i in range(len(s)):
    if s[i]=='A':
        flg_a =1
    elif s[i]=='B':
        flg_b =1
    elif s[i]=='C':
        flg_c =1
    else: pass
    
    if flg_a == 1  and flg_b == 1 and flg_c == 1:
        print(i+1)
        exit()
    else: continue