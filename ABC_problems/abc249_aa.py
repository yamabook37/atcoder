A,B,C,D,E,F,X = map(int, input().split())
Taka=0
Taka_T=0
Ao=0
Ao_T=0
cnt_w=0
cnt_b =0
lim = X

while(1):
    if lim >= 0:
        lim -= A
        #print(lim)
        Taka += A*B
        if lim-C >= 0:
            lim -= C
            #print(lim)
        else:
            break
    else:
        break
#print(Taka)

lim = X
while(1):
    if lim >= 0:
        lim -= D
        #print(lim)
        Ao += D*E
        if lim-F >= 0:
            lim -= F
            #print(lim)
        else:
            break
    else:
        break
#print(Ao)

if Taka > Ao:
    print("Takahashi")
elif Taka == Ao:
    print("Draw")
else:
    print("Aoki")
