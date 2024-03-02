N=int(input())
A=list(map(int, input().split()))

# -1の次に探すのは、A_i=xとなるi
# N回Aを探しに行くのは遅いので、A,iを保存できるデータ構造を使いたい
B = [-1]*N
pos = 0

for i in range(N):
    if A[i] == -1:
        pos = i
    else:
        # Bの値->i, インデックス->A
        # 0-indexにするために-1する
        B[A[i]-1] = i
# print(B)

ans = [pos+1]
for i in range(N-1):
    pos = B[pos]
    ans.append(pos+1)
print(*ans)
