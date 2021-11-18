N = int(input())
S = [int(i) for i in input().split()]
#print(S)

pre =[]
cnt = 0
#a,bは正の整数
for a in range(1,1001):
  for b in range(1,1001):
    yoso = 4*a*b + 3*a + 3*b
    #print(type(yoso))
    pre.append(yoso)
    #a,bの入れ替えも成り立つ
#print(pre)

for i in range(N):
  if S[i] not in pre:
  # Sに含まれない結果を++
    cnt += 1
print(cnt)