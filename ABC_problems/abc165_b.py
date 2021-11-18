import math
X=int(input())
temp = math.floor(100*0.01)
#print(temp+100)
for i in range(2,1000000000):
  temp += math.floor((100+temp) * 0.01)
  #print(temp+100)
  if temp+100 >= X:
    print(i)
    exit()

