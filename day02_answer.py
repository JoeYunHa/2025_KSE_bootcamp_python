import math

def my_power(base , expo) -> float :
    """
     A user-defined function that receives a base and exponent
     and returns the power result in the form of a real number
    :param base: base number
    :param expo: exponent
    :return: the power result in the form of a real number
    """
    result = 1

    integer_part = int(expo)
    fraction_part = expo - integer_part

    for _ in range(integer_part): # for k in range(expo)
        result *= base

    if fraction_part > 0:
        result *= math.exp(fraction_part * math.log(base))

    return result

def is_prime(num) -> bool :
    """
    A function that returns True if it is a prime number
    and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while i < (int(my_power(num,0.5)) + 1):
            if num % i == 0:
                return False
            i += 1
    else:
        return False
    return True

numbers = input("Input number : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <n2:
    if is_prime(j):
        print(j,end=' ')
    j += 1

