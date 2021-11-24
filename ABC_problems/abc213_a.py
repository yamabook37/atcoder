'''
Pythonのビット演算子
論理積（AND）: & 演算子
論理和（OR）: | 演算子
排他的論理和（XOR）: ^ 演算子
'''

# XOR は 2 回やると元に戻る
# A xor C=B となる 0 以上の整数 C 
'''
A^C=B
A^A^C=A^B
where A^A=0
C=A^B
'''
A, B = map(int, input().split())
print(A^B)
