# sample 
# https://xef.hatenadiary.org/entry/20120629/p3
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from random import randint

N = 60  # 配列の数
y = np.random.rand(N)*100 # ランダムな列をソートする

# ここに処理を書く
def animated_func():
    ...
    # 描画更新
    for rect, h in zip(rects, x):
        rect.set_height(h)
    fig.canvas.draw()
    ...

fig = plt.figure()
win = fig.canvas.manager.window
win.after(50, animated_func)
plt.show()