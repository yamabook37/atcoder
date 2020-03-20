x = int(input())
flag = 1

while True:
    if x == 2:
        break
    for i in range(3, x):
    #print("i is " + str(i))
        if x % i == 0:
            flag = 0
            break
    if flag == 1:
        break
    else:
        flag=1
        x += 1
print(x)