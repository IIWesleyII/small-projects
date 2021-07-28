# Print integers 1 to N, 
# but print “Fizz” if an integer is divisible by 3
# “Buzz” if an integer is divisible by 5 
# and “FizzBuzz” if an integer is divisible by both 3 and 5
def fizz_buzz(n = 0):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(80)