def is_rolling(x):
    return False if x < 0 else str(x) == str(x)[::-1]

def list_rolling(n):
    ans=[]
    #1 <= x <= n
    for i in range(n, 0, -1):
        if is_rolling(i):
            ans.append(i)
            # print(i)
    return ans

n=int(input())
ans=0
i=1
while i**3 <= n:
    # print(f"{i},{i**3}")
    if (is_rolling(i**3)):
        ans = i**3
    i+=1
print(ans)