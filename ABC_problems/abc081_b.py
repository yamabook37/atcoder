import math
n = input()
# 入力が何個か
'''
方針：
N個の入力が全て偶数のとき，全ての数を2で割ったものに置き換える
この操作が何回できるか
'''
a = list(map(int, input().split()))
# 数字の入力，半角区切りでリストに入れる
ans = float("inf")
# 無限大の定義
for i in a:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") -1)
    # 一番小さいものを割る方が楽
    # bin()...引数は整数，先頭に0bがついた2進の文字列に変換して返す
    # .rfind(検索する文字列, 開始位置, 終了位置) で文字列の検索する

    # 奇数で操作をしないアルゴリズムは謎のまま
print(round(ans))

