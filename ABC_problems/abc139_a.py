S = [s for s in input()]
T = [t for t in input()]

cnt=0
for i in range(3):
    if S[i] == T[i]:
        cnt +=1
print(cnt)