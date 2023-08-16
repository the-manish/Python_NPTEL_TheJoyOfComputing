def magic_square(n):
    
    magicSquare=[]
    for i in range (n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)

    for i in range (n):
        
        for j in range(n):

         print(magicSquare[i][j],end="")
    print()
         

magic_square(3)