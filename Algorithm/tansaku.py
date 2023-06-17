#最短経路
ys,xs=2,2
yg,xg=4,5
a=['########', '#......#', '#.######', '#..#...#', '#..##..#', '##.....#', '########']
n=[(ys-1,xs-1)]
route={n[0]:0}
p=[[1,0],[0,1],[-1,0],[0,-1]]
count=1
while route.get((yg-1,xg-1),0)==0 and count != 10000:
    n2=[]
    for i in n:
        for j in p:
            np=(i[0]+j[0],i[1]+j[1])
            if a[np[0]][np[1]]=='.' and route.get(np,-1)==-1:
                n2.append(np)
                route[np]=count
    n=n2
    count+=1
print(n,route)

#深さ探索
q=[{1, 3}, {1, 4}, {9, 5}, {5, 2}, {6, 5},{3,5},{8,9},{7,9}]
count=0
while count!=10000:
    a=q.pop()
    for j in q:
        if len(j&a) != 0:
            j |=a
            count=0
            break
    else:q=[a]+q
    if count>len(q): break
    count+=1
    print(count,q)

#幅優先探索
n=7
pt=[[1, 2, 3], [0], [5, 0], [6, 0], [6], [2], [3, 4]]
def bfs(v):
    d=[-1]*n
    d[v]=0
    q=[v]
    c=1
    while q:
        q1=[]
        for i in q:
            for j in pt[i]:
                if d[j]==-1:
                    d[j]=c
                    q1.append(j)
        q=q1
        c+=1
        print(d,q)
    return d
print(bfs(0))