n = int(input())
p = [int(i) for i in input().split()]
'''
p.sort()
print(p)
print(p[1])
'''
ans=0
for i in range(1,n-1):
  if p[i-1]>p[i]>p[i+1] or p[i-1]<p[i]<p[i+1]:
    ans+=1
print(ans)

#単純2番めじゃなくて，これらの順列のうち
'''
5
1 3 5 4 2
'''