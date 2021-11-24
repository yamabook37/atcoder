List = [s for s in input().split()]

# list[0]で最初の要素, list[-1]で最後の要素
if List[0][-1] == List[1][0] and List[1][-1] == List[2][0]:
  print('YES')
else:
  print('NO')