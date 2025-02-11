import math

def is_prime(num) -> bool: # -> return type : type hint
    """
    return True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(help(is_prime))
# can use help function
n = int(input("Input number : "))


if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")