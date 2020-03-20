# 標準系自作ライブラリ
# [競プロ使用上の注意]この中から関数ごとコピーしてコードに貼ること，importエラー起きるから

import itertools

# ビット生成
def bit(L, n):
  #L = [0, 1] #生成する数字のリスト
  #n = 3 #生成するビット数
  bit_list = list(itertools.product(L, repeat=n))
  return bit_list
#print(bit([0,1],3))

# 階乗
def factorial(seq):
  fac = list(itertools.permutations(seq))
  return len(fac)

# 順列 nPr  = n! / (n-r)!
  # 順列の数は，呼び出し側でlenで出力
def ptr(seq, r):
  # seq 集団のリスト，この要素数がn
  # r 選ぶ数 
  ptr = list(itertools.permutations(seq, r)) #順列列挙 
  return ptr

# 組み合わせ nCr = n! / (n-r)!r!
  # 組み合わせの数は，呼び出し側でlenで出力
def ncr(seq, r):
  # seq 集団のリスト，この要素数がn
  # r 選ぶ数 
  ncr = list(itertools.combinations(seq, r)) #順列列挙 
  return ncr

