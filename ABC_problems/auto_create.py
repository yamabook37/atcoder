import os
CONTEST='abc306'
PATH='/Users/yuki/Develop/pythonProject/python3/Atcoder/ABC_problems'
LEAST=['a','b','c']
#LEAST=['a','b','c','d']

for i in range(len(LEAST)):
    name = CONTEST+'_'+LEAST[i]+'.py'
    f = open(PATH+'/'+name, 'w')
    f.close()
    print('===== Success for created '+name+' =====')
