def factorial(n):
    product=1
    '''
    Iterative version:
    for i in range(1,n+1):
        product=product*i
        '''
    
    #Recursive Version
    #fact(n)=n*fact(n-1)
    #fact(0)=1
    #Base case
    if n==0:
      return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number:"))
if n<0:
    print('Factorial is not defined on negative number')
else:
    f=factorial(n)
    print('Factorial of ',n,'is',f)