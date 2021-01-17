N=input()
#print(list(N))
for i in range(3):
  if N[i] in '7':
    print('Yes')
    exit()
print('No')