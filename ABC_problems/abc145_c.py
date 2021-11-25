'''
3
0 0
1 0
0 1

2
-879 981
-866 890
'''
import math

n = int(input())
x=[0]*n
y=[0]*n
sum = 0.0

for i in range(n):
    x[i],y[i] = map(int, input().split())

for i in range(n):
    for j in range(n):
        sum += math.sqrt(pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2))
        #print(x[i],y[i],x[j],y[j],sum)
print(sum/n)