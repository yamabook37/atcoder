# 2019/11/17 5min
import math
a,b = map(float, input().split())

o = math.ceil((b-1) / (a-1)) 
#　.ceil が切り上げするメソッド
print(o)