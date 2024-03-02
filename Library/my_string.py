# 回文 判定
# palindrome
def is_rolling(x):
    return False if x < 0 else str(x) == str(x)[::-1]