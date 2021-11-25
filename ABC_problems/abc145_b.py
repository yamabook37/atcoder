def SsSl(): return list(map(lambda x: x, input()))

n = int(input())
#List = [s for s in input().split()]
List = SsSl()

if n%2==1:
    print("No")
else:
    if List[0:(n//2)]==List[(n//2):]:
        print("Yes")
    else:
        #print(List[0:(n/2)])
        #print(List[(n/2):])
        print("No")