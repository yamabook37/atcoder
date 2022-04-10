N = int(input())
S = [0, '1']
#S[1]をとる

for i in range(1, N):
    s = S[i] + ',' +  str(i+1) + ',' +  S[i]
    S.append(s)
    #print(*S[i].split(','))

print(*S[N].split(','))