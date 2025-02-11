n = int(input("Input number : "))

is_prime = True

if n >= 2:
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0 :
            is_prime = False
            break
else:
    is_prime = False

if is_prime :
    print(f"{n} is Prime number!")
else:
    print(f"{n} is Not Prime number")
