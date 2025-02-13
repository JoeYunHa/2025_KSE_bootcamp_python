# SOLID
# OCP -> 개방 폐쇄 원칙
# Opened for 확장, Closed fir modification
# annotation , decorator

import time


def time_decorator(func): # closure
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"실행 시간 : {e - s : .4f} s")
        return r
    return wrapper

# @time_decorator
def factorial_repetition(n) -> int:
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result

number = int(input())
ft = time_decorator(factorial_repetition)
# s = time.time()
print(f"{number}! = {ft(number)}")
# e = time.time()
# print(e - s)
