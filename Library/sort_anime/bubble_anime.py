import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import randint

N = 60  # 配列の数
y = np.random.rand(N)*100 # ランダムな列をソートする

# ここに処理を書く
def animated_bubblesort():
  rects = plt.bar(range(N), y, 1)
  for i in range(len(y)-1):
    for j in range(len(y)-1, i, -1):
      if(y[j-1] > y[j]):
        t = y[j]
        y[j] = y[j-1]
        y[j-1] = t
        fig.canvas.draw()

      for rect, h in zip(rects, y):
        rect.set_height(h)

  fig.canvas.draw()

fig = plt.figure()
win = fig.canvas.manager.window
# 関数用の描画
win.after(50, animated_bubblesort)
plt.show()