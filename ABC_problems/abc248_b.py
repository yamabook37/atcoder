A,B,K=map(int,input().split())

i = 0
while(A*(K**i) < B):
    i += 1

print(i)