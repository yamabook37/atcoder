# O((n+1)!)
# Stable : No

import random
from typing import List

def in_order(numbers: List[int]) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    print(numbers)
    
if __name__ == '__main__':
    # l = [1, 5, 3, 6]
    nums = [random.randint(0,1000) for _ in range(5)]
    bogo_sort(nums)
