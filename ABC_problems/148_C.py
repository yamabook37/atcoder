from fractions import gcd

def lcm(a,b):
    return a*b//gcd(a,b)


A,B=map(int,input().split())
print(lcm(A,B))