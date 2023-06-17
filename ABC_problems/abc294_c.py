import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# AとBを併合してソートする
c = a + b
c.sort()

# Aの各要素がcの何番目にあるか調べる
a_rank = []
for ai in a:
    rank = bisect.bisect_left(c, ai)
    a_rank.append(rank + 1)

# Bの各要素がcの何番目にあるか調べる
b_rank = []
for bi in b:
    rank = bisect.bisect_left(c, bi)
    b_rank.append(rank + 1)

print(*a_rank)
print(*b_rank)
