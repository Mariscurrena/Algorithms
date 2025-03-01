import random
import time
from text_format import formats as fmt

def quicksort(arr):
    # Base Case
    if len(arr)<2:
        return arr
    # Recursive Case
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot] # Array for every value less or equal to pivot
        greater = [i for i in arr[1:] if i > pivot] # Array for every value greater than pivot
        # recursion
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    size = 100 # #O(nlog(n))
    arr = []
    for i in range(size):
        arr.append(random.randint(1,100))
    print(f"{fmt.red}Original Array: {arr}{fmt.ends}")
    start = time.time()
    print(f"{fmt.green}Sorted Array: {quicksort(arr)}{fmt.ends}")
    end = time.time()
    duration = end - start
    print(f"{fmt.yellow}----> Quicksort algorithm lates: {duration} seconds.{fmt.ends}")