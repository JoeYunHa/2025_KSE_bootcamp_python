def my_abs(n)->int:
    if n < 0:
        return -n
    return n

def my_fibonacci_recursion(n)->int:
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
        return my_fibonacci_recursion(n-2) + my_fibonacci_recursion(n-1)

def my_fibonacci_loop(n)->int:
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