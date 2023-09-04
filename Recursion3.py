''' 
Fibonacci Sequence:
0th fib no=0
1th fib no=1
2nd fib no=1
3rd fib no=2

'''

def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    
n=int(input('Enter a non-negative number'))
if n<0:
    print('Fibonacci numbers are undefined for negative numbers')
else:
    print('Fibonacci number at position ',n, 'is',fibonacci(n))
   