# recursion
# import time
#
# def time_decorator(func):
#     def wrapper(*args):
#         s = time.time()
#         r = func(*args)
#         e = time.time()
#         print(f"{e - s} s")
#         return r
#     return wrapper

# @time_decorator
def fibonacci_recursion(n)->int:
    """
    Return fibonacci by recursion
    :param n: integer number
    :return: fibonacci(n)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

# @time_decorator
def fibonacci_loop(n)->int:
    """
    Return fibonacci by loop
    :param n: integer number
    :return: fibonacci(n)
    """
    res = 0
    a = 0
    b = 1
    i = 1
    while i < n :
        res = a+b
        a = b
        b = res
        i += 1
    return res

number = int(input("number : "))
print(fibonacci_recursion(number))
print(fibonacci_loop(number))

# time_decorator -> recursion마다 실행됨
