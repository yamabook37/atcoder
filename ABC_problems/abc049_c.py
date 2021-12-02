#DayDream 白昼夢
# S=T すなわちSを削除していってTにできるか
S=input()
# 順番に消していく、置き換える順番がある、この順にしないとダメ
ans = S.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
#print(ans)

#全て消せればnone <- False
if ans:
  print("NO")
else:
  print("YES")