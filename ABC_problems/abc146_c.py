A,B,X = map(int, input().split())

if A + B > X:
    print(0)
    exit()
elif A * (10**9) + B * 10 <= X:
    print(10**9)
    exit()
else: #範囲を絞る
    l=1
    r=10**9

    while r-l>1: #ここ大事r>lだとl=3,r=4で無限ループ，r-l >1だと通る
    #d = len(str(N))
        mid = int((l+r)/2)
        ans = A*mid + B*len(str(mid))
        if l==r:
            break
        elif ans <= X: #買えた時
            l = mid
        else:
            r = mid
    print(l)