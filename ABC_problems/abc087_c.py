N=int(input())
A1= list(map(int, input().split()))
A2= list(map(int, input().split()))
ans = [0]*N
for i in range(N):
  ans[i] += sum(A1[:i+1])
  #print(i,':', 'sum:',ans[i])
  ans[i] += sum(A2[i:])
  #print(i,':', 'sum:',ans[i])
print(max(ans))
