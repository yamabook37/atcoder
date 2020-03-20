n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
#print(a)

for i in range(n):
    for j in range(n):
        b.append(((a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2)**0.5) #root忘れず
#print(b)

#平均
print((sum(b)/(len(b)-n)) *(n-1))
    # 同一座標のものを除外して平均

'''
-879 981
-866 890

3
0 0
1 0
0 1
'''