import random
import time
from text_format import formats as fmt

def sum(arr):
    ## Base Case
    if len(arr) == 0:
        return 0
    ## Recursion Case
    else:
        return arr[0] + sum(arr[1:])
            
if __name__ == '__main__':
    arr = []
    size = 10
    for i in range(size):
        arr.append(random.randint(1,100))
    print(f"{fmt.red}Original array is: {arr}{fmt.ends}")
    start = time.time()
    print(f"{fmt.green}Array summatory value is: {sum(arr)}{fmt.ends}")
    end = time.time()
    duration = end - start
    print(f"{fmt.yellow}----> DyC lates: {duration} seconds.{fmt.ends}\n\n")