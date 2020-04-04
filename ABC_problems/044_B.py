w=list(input())
if all(w.count(i)%2==0 for i in set(w)):
  print('Yes')
else:
  print('No')