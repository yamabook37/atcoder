S=input()
n=len(S)
left=int((n-1)/2)
right=int((n+3)/2)
#rint(right)
cnt=0
for a, b in zip(S[:left], reversed(S[left+1:])):
  #print(a,b)
  if a == b: 
    cnt += 1
if cnt==left:
  flag=1

  cnt=0
  for a, b in zip(S[right-1:], reversed(S[:n])):
    #print(a,b)
    if a == b: 
      cnt += 1
    #print(cnt)

  if cnt== left:
    print('Yes')
    exit() 
print("No")
