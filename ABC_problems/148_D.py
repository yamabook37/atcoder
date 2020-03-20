#未完成
N =int(input())
I = [int(i) for i in input().split()]
Is=I #コピー

Is.sort()
#print(Is)

Imax=0
flg=0
for i in range(N-1):
    if (Is[i] < Is[i+1]):
        Imax +=1
        flg=1
    else:
        Imax=0

#Imaxになるまで続ける
cnt=0
temp=1
for i in range(N-1):
    if temp < I[i]:
        cnt+=1
    #elif temp == I[i]:
        #temp=I[i+1]
#print(cnt)

#判定
if N==1:
    print(0)
elif (flg==0)&(Imax==0):
    print(-1)
else:
    print(cnt)

'''
10
3 1 4 1 5 9 2 6 5 3

3
2 1 2
'''