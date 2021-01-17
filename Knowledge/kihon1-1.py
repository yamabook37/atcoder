'''
 参考 Atcoderで始めるPython入門
 https://qiita.com/KoyanagiHitoshi/items/3286fbc65d56dd67737c#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB
これを元に勉強していく
'''

# 1-1

#出力
print(10,20, sep=":")
# sep=""は区切り文字の指定，通常は半角スペース
# end=""は末尾の文字の指定，通常は改行

# 文字列の出力は ""か''で囲む
s = "Hello World"
print(s[2])

# リストの扱い
Lists = [1,2,3,4,5]
print(Lists)

# 1次元リストの各要素を出力：forループで吐き出す
for i in Lists:
    print(i)

# 1次元リストをアンパックして出力するとき，リストに*をつける
# アンパック：要素をリストとしてまとめて代入：リストのカッコを外す
print("アンパック", *Lists)
#bool(*Lists)

# 1次元リストの各インデックスの出力
List2 = [1,2,3,4,5]
for i in range(len(List2)):
    print(List2[i])

