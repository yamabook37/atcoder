x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

if x.count(min(x)) == 2:
    x4 = max(x)
else:
    x4 = min(x)

if y.count(min(y)) == 2:
    y4 = max(y)
else:
    y4 = min(y)

print('{} {}'.format(x4, y4))