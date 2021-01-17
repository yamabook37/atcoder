H,W,K = map(int,input().split())

in_li=[]
for i in range(H):
  c=list(input())
  in_li.append(c)
  new=list(in_li)
#print(in_li)
print(new)

cnt=0
for x in range(H):
  print(new[x].count('#'))
  for y in range(W):
    #print(new[x][y].count('#'))
    #ループのたびにカウントは間に合わない気がする
    pass
print(new.count('#'))


'''
2 3 2
..#
###
'''
