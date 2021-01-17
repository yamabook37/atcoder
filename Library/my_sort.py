# bubble
def bubble(num):
  # 方針
  # 後ろから順に隣り合う要素を比較する。
  # 左が右の要素に比べ大きい場合交換。
  # 走査範囲を前からひとつ狭める。
  for i in range(len(num)-1):
    for j in range(len(num)-1, i ,-1):
      if num[j] > num[j-1]:
        tmp = num[j-1]
        num[j-1] = num[j]
        num[j] = tmp
      print(num)

  return num

array = [2, 3, 5, 4, 1]
print(bubble(array))