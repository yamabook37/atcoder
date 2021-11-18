n,m=map(int, input().split())
maru=0
pena=[0]*n

Num = []
St = []

toi=set() #重複無しのset型で用意，リストの重複がないやつ
for i in range(m):
    p, s = input().split()
    #Num.append(int(p))
    #St.append(s)
#print(Num[0])
#print(St)
    p=int(p)-1 #0index

    if p in toi:
        continue #以降はスキップ

    elif s=='AC':
        toi.add(p) #そのpの時のとい番号を保存
        #print(p)
    else: 
        pena[p]+=1
print(len(toi), sum(pena[p] for p in toi)) #各pの時のWAをたす
    
'''
2 5
1 WA
1 AC
2 WA
2 AC
2 WA

100000 3
7777 AC
7777 AC
7777 AC

2 5
1 AC
1 AC
2 WA
2 AC
2 WA

2 5
1 AC
1 AC
2 WA
2 AC
2 AC

2 5
1 AC
2 AC
3 AC
4 AC
5 AC

'''
