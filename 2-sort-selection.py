#### Selection Sort
#### Searching in the list and then adding to another sorted list
#### O(nxn) = O(n^2) It is not so fast
import random
import time
from text_format import formats as fmt
#### Look into all the original list for the smallest value O(n)
def smallestfinding(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return int(smallest_index)

#### Creating tyhe sorted list
def sortselection(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = smallestfinding(arr)
        newArr.append(arr.pop(smallest)) ## Adding the smallest value to the sorted array into last position and removing from the original list.
    return newArr

if __name__ == '__main__':
    arr = []
    size = 100 #O(n^2) = O(20^2) = 400
    for i in range(size):
        arr.append(random.randint(1,100))
    print(f"{fmt.red}Original list is: {arr}{fmt.ends}")
    start = time.time()
    print(f"{fmt.green}Sorted list is:   {sortselection(arr)}{fmt.ends}\n")
    end = time.time()
    duration = end - start
    print(f"{fmt.yellow}----> Selectionsort algorithm lates: {duration} seconds.{fmt.ends}")