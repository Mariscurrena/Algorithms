### Recursion concepts that are useful for well known algorithms
### Every recursive function has two parts: The base case and the recursive case

########################## First Example ##################################
# import time
# def printing(tm):
#     print(".")
#     time.sleep(tm)

# def counter(number):
#     print(number)
#     time.sleep(0.15)
#     printing(0.15)
#     printing(0.15)
#     ### Base Case
#     if number < 1:
#         return
#     elif number == 1:
#         print("PUM!")
#     ### Recursive Case
#     else:
#         counter(number-1)


# if __name__ == '__main__':
#     number = 5
#     counter(number)

########################## Second Example ##################################
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
if __name__ == '__main__':
    for num in range(10,1,-1):
        print(f"{num}! is: {factorial(num)}")