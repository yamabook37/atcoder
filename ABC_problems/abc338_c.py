# Ax+By <= Qにおいて(x+y)の取りうる最大値
INF=10**18
N=int(input())
Q=list(map(int, input().split()))
A=list(map(int, input().split()))
B=list(map(int, input().split()))

ans=0
# xを固定しyのみ動かす
for x in range(max(Q)+1):
    y=INF
    for i in range(N):
        # Ax+By <= Qより y <= (Q-Ax)/B
        # B=0の時、0除算になるので割らずにスキップ
        if A[i]*x > Q[i]:
            y = -INF
        elif B[i] > 0:
            y = min(y, (Q[i]-A[i] * x) // B[i])
    ans = max(ans, x+y)
print(ans)