N = int(input())
evi = []

for i in range(N):
    A = int(input())
    X = [list(map(int, input().split())) for i in range(A)]
    #print(X[i])
    evi.append(X)

#めっちゃむずい，bit全探索　を勉強してからかく


'''
3
1
2 1
1
1 1
1
2 0
'''