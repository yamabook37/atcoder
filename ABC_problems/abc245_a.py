a,b,c,d=map(int,input().split())

if a < c:
    print('Takahashi')
    exit()
elif a > c:
    print('Aoki')
    exit()
elif a==c:
    if b <= d:
        print('Takahashi')
    else:
        print('Aoki')

