N=int(input())
S = ['AC', 'WA', 'TLE', 'RE']
li=[]

for i in range(N):
  jud = input()
  li.append(jud)
a=li.count('AC')
w=li.count('WA')
t=li.count('TLE')
r=li.count('RE')

#print(li)
#print(a)

print('AC x '+str(a))
print('WA x '+str(w))
print('TLE x '+str(t))
print('RE x '+str(r))

'''
6
AC
TLE
AC
AC
WA
TLE
'''