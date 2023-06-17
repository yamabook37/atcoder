n = int(input())
socks = list(map(int, input().split()))

sock_counts = {}
for sock in socks:
    if sock in sock_counts:
        sock_counts[sock] += 1
    else:
        sock_counts[sock] = 1

pair_count = 0
for sock_count in sock_counts.values():
    pair_count += sock_count // 2

print(pair_count)
