# squares = list()
# for i in range(1,6,1):
#     squares.append(i*i)
# print(squares)

# list comprehension
# com_squares = [i*i for i in range(1,6,1)]
# print(com_squares)
#
# even_squares = [i*i for i in range(1,6,1) if i % 2 == 0]
# print(even_squares)
#
# odd_squares = [i*i for i in range (1,6,1) if i % 2 != 0]
# print(odd_squares)

# dictionary
# sugang = dict(python="kim", cpp="sung", db="kang")
sugang = {'python': 'kim', 'cpp': 'sung', 'db' : 'kang'}
print(sugang)
sugang['datastructure'] = 'kim' # add
print(sugang)
sugang['datastructure'] = 'park' # update
print(sugang)
print(sugang['db'])
# function get => search by key, return value
# if not exists => return second parameter
print(sugang.get('db'))
print(sugang.get('opensource'))
print(sugang.get('cpp','not exist'))

# items()
for i in sugang.items():
    print(i)

for k in sugang.keys():
    print(k)

for v in sugang.values():
    print(v)