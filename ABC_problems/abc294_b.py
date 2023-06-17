h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
for i in range(h):
    s = ''.join([chr(ord('A')+a[i][j]-1) if a[i][j] != 0 else '.' for j in range(w)])
    print(s)