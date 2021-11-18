N = int(input())
H = list(map(int, input().split()))

for i in reversed(range(N)):
    if i == 0:
        continue
    elif H[i-1]>H[i-1-1]:
        if H[i-1] -H[i-2] ==1:
            H[i-1] -= 1
    else:
        print('No')
        exit(0)
print('Yes')

# 未完成