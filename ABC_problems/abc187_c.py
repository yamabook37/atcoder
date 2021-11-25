N = int(input())

# ある文字列が、集合の中に存在するかどうか
# 存在確認をO(1)で行いたいのでset型、Listでは O(N2)
S = set()  

# N個の受け取り
for _ in range(N):
  temp = input()
  S.add(temp)  
  # setに追加するのはappendではなく、add
#print(S)

def solve():
  # 外：!を0文字付加
  for T in S:
    # 中：!を1文字付加
    if "!" + T in S:
    # Tが不満な文字列
      return T
  return "satisfiable"
  # 関数は返り値を返して終わるのでexit()いらない

print(solve())

