
# function
#correct logic!
def FizzBuzz(r): 
 for i in range(1,r):
    if(i%3==0 and i%5==0):
       #  print(i,"FizzBuzz")
      print(str(i)+" FizzBuzz")
      
    else :
        if(i%3==0):
         # print(i,"Fizz")
         print(str(i)+" Fizz")
           
        else:
            if(i%5==0):
              #print(i,"Buzz")
              print(str(i)+" Buzz") 
            else:
                print(str(i))

FizzBuzz(51)