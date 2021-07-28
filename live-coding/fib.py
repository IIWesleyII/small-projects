


# Fn =Fn-1 + Fn-2
# returns fib number of n in O(2^n)
# sloooooooooooooooow
def fib(n):
    
    if n <= 0:
        return 0
    elif n== 1:
        return 1
    return (fib(n-1) + fib(n-2))

#print(fib(58))

#returns fib list in O(n)
def fib_lst(n):
    lst = [0,1]
    i = 1
    while i != n:
        lst.append(lst[i-1]+lst[i])
        i += 1
    return lst

print(fib_lst(5))