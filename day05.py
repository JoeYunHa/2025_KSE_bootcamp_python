# recursion

def factorial_recursion(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n-1)

number = int(input("number : "))
print(factorial_recursion(number))

