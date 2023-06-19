n,m,h,k = map(int,input().split())
s = input()
pair = set(tuple(map(int,input().split())) for _ in range(m))
#print(n,m,h,k)

x = 0
y = 0
for i in s:
    if i == 'R':
        x += 1 
    elif i == 'L':
        x -= 1
    elif i == 'U':
        y += 1
    elif i == 'D':
        y -= 1
    h -= 1
    if h < 0:
        print('No')
        break
    if h < k:
        if (x,y) in pair:
            h = k
            pair.remove((x,y))
if h >= 0:
    print('Yes')

'''
4 2 3 1
RUDL
-1 -1
1 0
'''