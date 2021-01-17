N=int(input())
for i in range(100):
  if i*1000 >= N:
    print(1000*i - N)
    exit()