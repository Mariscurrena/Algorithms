## Binary search only works for sorted lists

#### Logarithmic Example
# import math
# def binary(number):
#     return(math.log2(number))

# number = 8
# print(binary(number))

import random
import math
import os
os.system('cls')
#### Binary Search
def binary_search(list, item):
    low = 0
    high = len(list)-1
    tries = 0
    while low <= high:
        mid = int((low+high)/2)
        guess = list[mid]
        tries += 1
        if guess == item:
            return f"Number is: {item}, position: {mid}, tries: {tries}"
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ =='__main__':
    mylist = []
    rng = 100000000
    print(math.log2(rng))
    for i in range(int(rng)):
        mylist.append(i+1)
    print(f"{binary_search(mylist, random.randint(1,rng))}, log2({rng})={math.log2(rng)}\n")