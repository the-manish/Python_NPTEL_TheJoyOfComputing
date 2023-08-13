import random
def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    print (p)
    if (p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'

with open("dna_data.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,10000):
    evolve(x)
print(x)