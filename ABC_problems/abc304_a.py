n = int(input())
pair = [tuple(input().split(' ')) for i in range(n)]
#print(pair[0][1])

m=10**9
index=0
for j in range(n):
    #print(int(pair[j][1]),m)
    tm = min( int(pair[j][1]), m)
    if tm < m:
        m = tm
        index = j

for k in range(n):
    print(pair[(index+k)%n][0])

'''
5
alice 31
bob 41
carol 5
dave 92
ellen 65
'''