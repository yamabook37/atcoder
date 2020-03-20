# 数学系自作ライブラリ
# [競プロ使用上の注意]この中から関数ごとコピーしてコードに貼ること，importエラー起きるから

import math

# 最大公約数 gcd(a,b)はmathからimport
def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

# 最小公倍数
def lcm(a, b):
  return a*b // math.gcd(a,b)

# 素数の判定 True or False
def is_prime(n):
  for i in range(2, n+1):
    if i*i > n:
      break
    if n%i == 0:
      return False
  return n != 1

# 約数の列挙
def divisor(n):
  i = 1
  ans = []
  # root(N)まで回す
  while i*i <= n:
    if n%i == 0:
      ans.append(i)
      # 割れたら追加
      ans.append(n//i)
    i += 1
  ans = [set(ans)]
  #setで重複を除外する
  return ans

# 素数列挙
def eratosthenes(n):
  is_prime = [True for _ in range(n+1)]
  # n+1個全てTのリスト
  is_prime[0] = False

  for i in range(2, n+1):
    if is_prime[i-1]:
      j = 2 * i
      while j <= n:
        is_prime[j-1] = False
        j += i
  ans = [ i for i in range(1, n+1) if is_prime[i-1]]
    # Trueのみを抽出
  # is_prime には真偽の情報N+1個のリスト, 0:F 1-n:TorF
  return ans

# 素因数分解 ,nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  ans = []
  while i * i <= n:
    # 割れる限りわる
    while n % i == 0:
      n /= i
      ans.append(i)
    i += 1
  # 割終えた残り, n=1なら終わり，n>1ならそのnも入れる
  if n > 1:
    ans.append(int(n))
  return ans


#print(eratosthenes(5))