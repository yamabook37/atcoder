a, b, k=map(int, input().split())

if a>=k:
    a = a-k
    k = 0
    print(a,b)
elif a<k:
    k = k-a
    a = 0
    print(0, max(0,b-k))

#10^12あるので，ループ回してたら間に合わない