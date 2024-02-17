##### DEBUG #####
import sys
def error(*args, end="\n"): print(*args, end=end, file=sys.stderr)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
##### DEBUG #####

from functools import lru_cache
@lru_cache
def f(x):
    if x==1:
        return 0
    else:
        return f(x // 2) + f((x+1) // 2) + x

print(f(int(input())))