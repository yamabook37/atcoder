s=input()
n=len(s)
for i in range(n):
    diff=True
    for j in range(n):
        if (s[i] == s[j]) & (i != j):
            diff=False

    if diff == True:
        print(i+1)