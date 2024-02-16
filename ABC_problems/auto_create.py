import os
PATH='/Users/yuki/Develop/pythonProject/python3/Atcoder/ABC_problems'
CONTEST='abc341'
LEAST=['a','b','c']
#LEAST=['a','b','c','d']

content = ('##### DEBUG #####\n'
    'import sys\n'
    'def error(*args, end="\\n"): print(*args, end=end, file=sys.stderr)\n'
    'if len(sys.argv) == 2:\n'
    '    sys.stdin = open(sys.argv[1])\n'
    '##### DEBUG #####\n')

for i in range(len(LEAST)):
    name = CONTEST+'_'+LEAST[i]+'.py'
    f = open(PATH+'/'+name, 'w')
    f.write(content)
    f.close()
    print('===== Success for created '+name+' =====')
