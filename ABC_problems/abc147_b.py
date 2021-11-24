S = list(input())
#print(S)

n = len(S)
# 端と端から同じものに合わせていく
cou = 0
for i in range(n//2):
    if S[i] != S[n-1-i]:
        S[n-1-i] = S[i]
        cou += 1
    else:
        continue
#print(S)
print(cou)
