'''
2019/09/06 from Musyano
計算量の概算
https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0#%E4%BE%8B-14-%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E3%81%B5%E3%82%8B%E3%81%84-on-loglogn
'''

import time

N = 5 #何桁まで判定できるプログラムにしたいか
MAX = 10**N

#iが素数だったら1(True)を、合成数であったら0(False)を返す配列を作ればよい
is_prime = [1]*MAX #最初は1(True)を入れておく
is_prime[0] = 0
is_prime[1] = 0 #[0]と[1]は当然非素数だからFalse

for i in range(2,MAX):
    if is_prime[i] == 0:#もしもiが素数じゃなかったら
        continue #次の操作は行わず次のiの判定へ
    for j in range(i*2, MAX, i): #iが素数なら2i,3i,...は⇒
    # 見つけた素数の倍数をふるい落す
        is_prime[j] = 0 #合成数

input_number = int(input('好きな数字を入力してください：'))

start = time.time()
if is_prime[input_number]:
    print(str(input_number) + 'は素数です')
else:
    print(str(input_number) + 'は合成数です')

elapsed_time = (time.time() - start) *10.0**3
print(f"{elapsed_time}" + "[m sec]")
