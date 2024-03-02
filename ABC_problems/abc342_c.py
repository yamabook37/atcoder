from string import ascii_lowercase

N=int(input())
S=input()
Q=int(input())

# 変換前と変換後の文字列を作る
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz' で初期化
# https://docs.python.org/ja/3/library/string.html
mapping_from = ascii_lowercase
mapping_to = ascii_lowercase
for _ in range(Q):
    c, d = input().split()
    mapping_to = mapping_to.replace(c, d)
    # print(mapping_to)

# 対応する文字をそれぞれ置き換える, O(1)のみ
## str.translate() 辞書を渡す
## str.maketrans()関数には置換元文字をキー、置換先文字列を値とする辞書を指定
print(S.translate(str.maketrans(mapping_from, mapping_to)))