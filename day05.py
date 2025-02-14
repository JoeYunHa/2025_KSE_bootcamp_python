# yield

def my_range(first=0,last=5,step=1):
    number = first
    while number < last:
        yield number # number 를 return 한 다음에도 나머지 함수 구문을 수행
        number += step
# memory 절약
r = my_range()
print(r,type(r))

for x in r:
    print(x)
for x in r:
    print(x)
