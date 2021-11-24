S = input()

day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
ss = 0
for i in range(7):
    if S==day[i]:
        ss = abs(7-i)

print(ss)