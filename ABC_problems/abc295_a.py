n=int(input())
w=list(input().split())
st=['and', 'not', 'that', 'the', 'you']
for i in range(n):
    if w[i] in st:
        print("Yes")
        exit()
print("No")