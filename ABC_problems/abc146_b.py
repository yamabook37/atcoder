def caesar(s, n):
    ns = []
    for ch in s:
        # A - Z
        if ('A' <= ch and ch <= 'Z'):
            ns.append(chr((ord(ch) - ord('A') + n) % 26 + ord('A')))
            # nの符号で向き変更
            # ord() でUnicodeのポインタを返す,chr()はその逆
            # %26 とすることで，26,27は1,2のようにまた循環できる
        # 0 - 9
        elif ('0' <= ch and ch <= '9'):
            ns.append(chr((ord(ch) - ord('0') - n) % 10 + ord('0')))
        # no change for other characters
        else:
            ns.append(ch)
    return "".join(ns)

N = int(input())
S = input()

print(caesar(S, N))

'''
13
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''