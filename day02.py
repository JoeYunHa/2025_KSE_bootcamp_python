import math

def is_prime(num):
    if num >= 2:
        for i in range(2, int(math.sqrt(num))):
            if num % i == 0:
                return False
        return True
    else:
        return False

n = int(input("Input number : "))


if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")