from decimal import Decimal, getcontext, ROUND_HALF_UP
# decimalモジュールのDecimalクラスとそのquantizeメソッド

X = input()
# 文字列で受け取る
ans = Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(ans)