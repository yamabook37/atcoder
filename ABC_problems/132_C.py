N=int(input())
d=list(map(int,input().split()))
d.sort() #値を返さないNone
#print(d)
print(d[N//2] - d[N//2 -1])