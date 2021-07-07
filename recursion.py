#facorial examples
def fac(n):
    return n if n == 1 else n * fac(n - 1)

print(f"{fac(5)}\n")

from math import factorial
print(factorial(5))