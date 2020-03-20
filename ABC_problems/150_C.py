import itertools as it

N=int(input())
P=tuple(map(int,input().split())) #値変更できないようにタプルで用意
Q=tuple(map(int,input().split()))

l=[n for n in range(1,N+1)] #Nまでのリスト
p=list(it.permutations(l)) #Nまでのリストから，順列のリストを作成
a=p.index(P);b=p.index(Q) #pのうちP,Qのインデックスを取得
ans=abs(b-a)

print(ans)