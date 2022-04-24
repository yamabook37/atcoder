def has_duplicates(seq):
    return not(len(seq) != len(set(seq)))
    # ユニークならfalse

S = list(input())
#L=["a","b","c","A","B"]
#print(has_duplicates(L))
num = len(S)
#print(S[0], num)

small = False
big = False

for i in range(0,num):
    if S[i].islower():
        small = True
        #print(S[i], "low")
    if S[i].isupper():
        big = True
        #print(S[i], "up")
        
if (small and big) and (has_duplicates(S)):
    print("Yes")
else:
    print("No")



