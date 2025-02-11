def my_pow(base , exp) -> int :
    ans = 1
    for j in range(0,exp):
        ans *= base
    return ans
first , second = input("Input two number a, b (a < b) : ").split()

a = int(first)
b = int(second)

if a > b:
    a , b = b , a

num = a

while num <= b:
   if num >= 2 :
       is_prime = True
       i = 2
       while my_pow(i,2) <= num :
           if num % i == 0:
               is_prime = False
               break
           i += 1
       if is_prime :
           print(num , end = ' ')
   num += 1









