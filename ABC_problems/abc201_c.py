def main():
  # 判別用関数
  def judge(s):
    for o in O:
      # oはsに確実に含まれている
      if o not in s:
        return False
    
    for x in X:
        # xはsに確実に含まれていない
      if x in s:
        return False
    return True


  S = input()
  O = []
  X = []

  for i, char in enumerate(S):
    if char == "o":
      O.append(str(i))
    elif char == "x":
      X.append(str(i))

  ans = 0

  # 10^4通り試す
  for i in range(10000):
    # str型で4桁の "0000"～"9999"を生成
    s = str(i).zfill(4)
    if judge(s):
      ans += 1

  print(ans)


if __name__ == '__main__':
  main()
