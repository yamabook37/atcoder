s=input()
up_flg = False
low_flg = True
if s[0].isupper():
    up_flg = True
for i in range(1,len(s)):
    if not(s[i].islower()):
        low_flg = False
        
if up_flg and low_flg:
    print("Yes")
else:
    print("No")