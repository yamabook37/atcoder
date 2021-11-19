S = input()
# S は等しい2文字とそれとは異なる1文字
ans = 3
# 同種なら1
if S[0] == S[1] and S[1] == S[2]:
  ans = 1
# 異種なら 3!=6
elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
  ans = 6
print(ans)