X=int(input())
u1=X//500
#print(u1*1000)
u2=(X%500)//5
#print(u2*5)
print(u1*1000 + u2*5)