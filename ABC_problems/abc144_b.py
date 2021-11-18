n = int(input())
flag = 0

for i in range(1,10):
    for j in range(1,10):
        if i*j == n:
            flag = 1

if flag == 1:
    print("Yes")
else:
    print("No")