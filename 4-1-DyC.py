import random

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
    print(f"Original array is: {arr}")
    print(f"Array summatory value is: {sum(arr)}\n\n")