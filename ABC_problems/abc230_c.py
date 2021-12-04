N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

H = Q - P + 1
W = S - R + 1

#i=A+k かつ、 j=B+k
#i=A+k  かつ、j=B−k

for i in range(P, Q + 1):
    ans = []  # 文字列の連結が遅いPyPyでは、文字列を+=で連結するとTLEになる
    for j in range(R, S + 1):
        if (i - j == A - B) or (i + j == A + B):
            ans.append("#")
        else:
            ans.append(".")
    #print(ans)
    print(*ans, sep="")

'''
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans_li = [["."] * (S - R + 1) for _ in range(Q - P + 1)]
for i in range(Q - P + 1):
    for j in range(S - R + 1):
        if (i + P) - A == (j + R) - B:
            ans_li[i][j] = "#"
        if (i + P) - A == B - (j + R):
            ans_li[i][j] = "#"

for ans in ans_li:
    print("".join(ans))
'''