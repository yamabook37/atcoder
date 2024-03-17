# N,M,Lの3重ループ *Q分の判定処理; O(100*100*100*10^5)=O(10^11) 
# -> 3重ループで作れる値をメモしておく, O(log NML)

n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))
l=int(input())
C=list(map(int, input().split()))

S=set()
for a in A:
    for b in B:
        for c in C:
            S.add(a+b+c)
            
q=int(input())
X=list(map(int, input().split()))

for x in X:
    if x in S:
        print("Yes")
    else:
        print("No")