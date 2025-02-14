# recursion

def count_down_recursion(n):
    if n == 0:
        print("boom!")
        return
    else:
        print(f"{n}!")
        return count_down_recursion(n-1)

def count_down_loop(n):
    while n > 0:
        print(f"{n}!")
        n -= 1
    print(f"BOOM!")
    return


num = int(input())
count_down_recursion(num)
count_down_loop(num)