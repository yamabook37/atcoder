N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    A,B = map(int, input().split())
    position_A = P.index(A)
    position_B = P.index(B)
    if position_A > position_B:
        print(B)
    else:
        print(A)