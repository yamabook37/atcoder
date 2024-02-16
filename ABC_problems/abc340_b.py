##### DEBUG #####
import sys
def error(*args, end="\n"): print(*args, end=end, file=sys.stderr)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
##### DEBUG #####

Q = int(input())
A = []
for i in range(Q):
    num,que = map(int,input().split())
    if num == 1:
        A.append(que)
    elif num == 2:
        print(A[-que])