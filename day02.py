import math

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
       while math.pow(i,2) <= num :
           if num % i == 0:
               is_prime = False
               break
           i += 1
       if is_prime :
           print(num , end = ' ')
   num += 1









