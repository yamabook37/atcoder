N = int(input())
#重複は消す
D = set()
for i in range(N):
  d = int(input())
  D.add(d)
print(len(D))
