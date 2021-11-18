n = int(input())
A = list(map(int, input().split()))

print('{:.16g}'.format(1 / sum(1 / x for x in A)))

'''
3
200 200 200
'''