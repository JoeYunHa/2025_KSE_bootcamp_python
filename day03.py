import math

def my_power(base , expo) -> float :
    """
     A user-defined function that receives a base and exponent
     and returns the power result in the form of a real number
    :param base: base number
    :param expo: exponent
    :return: the power result in the form of a real number
    """

    if expo < 0:
        base = 1 / base
        expo *= -1

    result = 1

    integer_part = int(expo)
    fraction_part = expo - integer_part

    for _ in range(integer_part): # for k in range(expo)
        result *= base

    if fraction_part > 0:
        result *= math.exp(fraction_part * math.log(base))

    return result

print(my_power(2,9))
# if expo is not integer
print(my_power(25,0.5))
# if expo < 0
print(my_power(10,-1))
