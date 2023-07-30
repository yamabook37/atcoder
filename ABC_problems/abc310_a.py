n,p,q=map(int,input().split(' '))
#print(n,p,q)

d=(input().split(' '))
d=list(map(int,d))
print(min(p,q+min(d)))

'''
3 100 50
60 20 40
'''