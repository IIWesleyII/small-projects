
import time
def fib(n):
    if n < 1:
        return -1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


start_time = time.time()
fib(30)
recursive_time = time.time() - start_time
print(f"recursion fibonacci = {recursive_time}")


def fib_faster(n):
    lst = [0,1]
    i = 1
    while i != n:
        lst.append(lst[i-1]+lst[i])
        i += 1
    return lst[-1]
start_time = time.time()   
fib_faster(30)
standard_time = time.time() - start_time

print(f"standard fibonacci = {recursive_time}")