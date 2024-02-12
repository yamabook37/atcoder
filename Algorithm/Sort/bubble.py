# O((n+1)!)
# Stable : No
# 区切りを(n-1)個目に挿入しその前の要素を順番にソート、終わると区切りの位置を1つ手前にずらし繰り返す

import random
from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_num = len(numbers)
    for i in range(0, len_num):
        # 区切り位置の指定
        for j in range(len_num - 1 -i):
            # print(f"position: {j}")
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == '__main__':
    # nums = [1, 8, 3, 5, 9]
    nums = [random.randint(0,1000) for _ in range(5)]
    bubble_sort(nums)
    print(nums)