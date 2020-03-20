N = int(input())
H = list(map(int, input().split()))

ans = 0
cnt = 0

# O(N)
for i in range(N-1):
    if H[i] >= H[i+1]:
        cnt += 1
    else:
        if ans < cnt:
            ans = cnt
        cnt = 0    
if ans < cnt:
    ans = cnt
print(ans) 
