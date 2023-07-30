def is_sim_char(c, d):
    return (c == d
        or (c == "0" and d == "o")
        or (c == "o" and d == "0")
        or (c == "l" and d == "1")
        or (c == "1" and d == "l")
    )
def is_sim_string(s, t):
    for i in range(len(s)):
        if not is_sim_char(s[i], t[i]):
            return False
    return True

n=int(input())
s=list(input())
t=list(input())
print('Yes' if is_sim_string(s, t) else 'No')