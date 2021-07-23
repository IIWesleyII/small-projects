


# Fn =Fn-1 + Fn-2
# returns fib number of n
def fib(n):
    
    if n == 0:
        return 0
    elif n== 1 or n==2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

#print(fib(30))

#returns fib list
def fib_lst(n):
    lst = [0,1]
    i = 1
    while i != n:
        lst.append(lst[i-1]+lst[i])
        i += 1
    return lst

print(fib_lst(9))