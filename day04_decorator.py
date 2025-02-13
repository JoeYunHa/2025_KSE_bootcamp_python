import time

def description(f):
    def wrapper(*args):
        print(f.__name__)
        print(f.__doc__)
        r = f(*args)
        return r
    return wrapper


def time_decorator(func):
    def wrapper(*args):
        s = time.time()
        r = func(*args)
        e = time.time()

        print(f"실행 시간 : {e-s} s")
        return r
    return wrapper

@time_decorator
@description
def factorial_repetition(n) -> int:
    """
    factorial function by loop
    :param n: integer number
    :return: result of factorial operation
    """
    result = 1
    for i in range(2,n+2):
        result *= i
    return result

num = int(input())

print(f"{num}! = {factorial_repetition(num)}")


