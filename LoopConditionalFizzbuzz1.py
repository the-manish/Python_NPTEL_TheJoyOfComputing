
for i in range(1,51):
    if(i%3==0):
       # print(i,"Fizz")
        print(str(i)+" Fizz")
    else :
        if(i%5==0):
            #print(i,"Buzz")
            print(str(i)+" Buzz")
        else:
            if(i%3==0 and i%5==0):
              #  print(i,"FizzBuzz")
                print(str(i)+" =FizzBuzz")
            else:
                print(str(i))

                #Incorrect logic as we see 15 is fizz but it must be FizzBuzz
        