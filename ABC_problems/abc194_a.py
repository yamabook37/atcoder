A, B = map(int, input().split())

if A+B >= 15 and B >= 8:
  print(1)
  exit()
elif A+B >= 10 and B >= 3:
  print(2)
  exit()
elif A+B >= 3:
#問題をよく読むこと
  print(3)
  exit()
else:
  print(4)

'''
乳固形分 = A 無脂乳固形分 + B 乳脂肪分
'''
