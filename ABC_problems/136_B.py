N = int(input())

flg=0
for i in range(1, N+1): #N以下
    keta = len(str(i))
    if keta % 2 ==1:
        flg += 1

print(flg)