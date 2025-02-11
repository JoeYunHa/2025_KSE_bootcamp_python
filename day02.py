
def is_prime(num) -> bool :
    """
    return True if it is a prime number and False if it is not a prime number
    :param num: integer number
    :return: boolean type
    """
    if num >= 2:
        i = 2
        while (i * i) <= num :
            if num % i == 0:
                return False
            i += 1
        return True
    else:
        return False

n = int(input("Input number : "))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")