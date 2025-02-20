import math, random

def binary_search_recursion(list, item, low=0, high=None):
    if high is None:
        high = len(list) - 1
    mid = int((low+high)/2)
    guess = list[mid]
    ### Base case
    if guess == item:
        return f"Number is: {item}, position: {mid}"
    ### Recursion Case
    elif guess > item:
        return binary_search_recursion(list,item,low,mid-1)
    else:
        return binary_search_recursion(list,item,mid+1,high)

if __name__ =='__main__':
    mylist = []
    rng = 1000
    #print(math.log2(rng))
    for i in range(int(rng)):
        mylist.append(i+1)
    print(f"{binary_search_recursion(mylist, random.randint(1,rng))}, log2({rng})={math.log2(rng)}\n")