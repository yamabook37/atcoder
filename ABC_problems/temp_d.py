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

N=int(input())
num=prime_decomposition(N)
print(num)
print(set(num))
print(len(num)-len(set(num)))