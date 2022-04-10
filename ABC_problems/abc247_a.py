S=input()
#print(S[0])

flag=0
if S[3] == "1":
  flag=1
#print(flag)

T=[0]*4
T[1]=S[0]
T[2]=S[1]
T[3]=S[2]
if flag==1:
  T[0]="0"
print(*T, sep="")

#22min

'''
#解説
S = input()
print("0" + S[:3])
#頭は常に0で、残りはシフトするだけ
'''