# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())

# スペース区切りの整数の入力 半角スペース区切り, 指定するにはsep=で指定
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))