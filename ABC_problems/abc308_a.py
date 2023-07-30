s = list(map(int, input().split()))

for i in range(8):
    if i < 7 and s[i] > s[i + 1]:
        print("No")
        exit()
    if s[i] < 100 or s[i] > 675 or s[i] % 25 != 0:
        print("No")
        exit()
print("Yes")