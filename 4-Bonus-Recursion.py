import math, random, time
from text_format import formats as fmt
from text_format import dict

def quicksort(arr):
    # Base Case
    if len(arr) < 2:
        return arr
    # Recursive Case
    else:
        pivot = arr[0]
        # Aquí comparamos por el 'id' de cada diccionario
        less = [i for i in arr[1:] if i['id'] <= pivot['id']]
        greater = [i for i in arr[1:] if i['id'] > pivot['id']]
        return quicksort(less) + [pivot] + quicksort(greater)

def binary_search(dict, item):
    low = 0
    high = len(dict) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = dict[mid]['id']
        # Base Case
        if guess == item:
            return dict[mid]
        # Recursive Case
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1  
    return None

if __name__ == '__main__':
    rng=len(dict)
    print(f"{fmt.blue}This is a exercise using recursion.{fmt.ends}")
    print(f"{fmt.blue}The objective is to receive an unordered list, sort it using a quicksort algorithm, and then find a random user in the list using a binary search algorithm with recursion.{fmt.ends}")
    print(f"{fmt.blue}Program will start in 5 seconds:{fmt.ends}\n\n")
    time.sleep(5)
    start = time.time()
    print(f"{fmt.green}{binary_search(quicksort(dict), random.randint(1,rng))}, log2({rng})={math.log2(rng)}{fmt.ends}")
    end = time.time()
    duration = end - start
    print(f"{fmt.yellow}----> Prueb recursion lates: {duration} seconds.{fmt.ends}\n")