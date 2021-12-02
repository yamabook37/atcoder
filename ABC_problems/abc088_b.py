N = int(input())
A = list(map(int, input().split()))
#print(A)

a = sorted(A, reverse=True)
#アリスは先にとるのでソートリストの初めから2ステップおきにsum
#ボブは1個ずらして
alice = sum(a[0::2])
bob = sum(a[1::2])
print(abs(alice - bob))