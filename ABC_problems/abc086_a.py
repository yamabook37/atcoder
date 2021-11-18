def Fizz_Buzz (number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
#本当のFizz_Buzzは３と５

a, b = map(int, input().split())
# 複数の整数の標準入力，半角スペース区切り
c = a*b
Fizz_Buzz(c)
