# Atcoder 入力テンプレート for python

## 整数 n
```python
n = int(input())
```

## 整数組 x y
```python
x,y = map(int, input().split(' '))
```

## 整数と改行なし数列 n / a1 ... an
```python
n = int(input())
a = list(map(int, input().split(' ')))
```

## 整数と改行あり整数 n / s1 / ... / sn
```python
n = int(input())
s=[]
s = [int(input()) for _ in range(n)]

for i in range(n):
    s.append(int(input()))
```

## 整数と改行あり整数組 n / x1 y1 / ... / xn yn
```python
n = int(input())
pair = [tuple(map(int, input().split(' '))) for i in range(n)]
```

```python
```

## Reference
https://harinez2.hateblo.jp/entry/atcoder-template-python#%E5%85%A5%E5%8A%9B-n--x1-y1----xn-yn