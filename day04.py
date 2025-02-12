squares = list()
for i in range(1,6,1):
    squares.append(i*i)
print(squares)

# list comprehension
com_squares = [i*i for i in range(1,6,1)]
print(com_squares)

even_squares = [i*i for i in range(1,6,1) if i % 2 == 0]
print(even_squares)

odd_squares = [i*i for i in range (1,6,1) if i % 2 != 0]
print(odd_squares)