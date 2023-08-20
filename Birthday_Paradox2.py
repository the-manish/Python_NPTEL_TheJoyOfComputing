import random
birthday=[]
i=0
while(i<50):
    year=random.randint(1895,2023)
    #The oldest person ever lived was 122 years old
    if (year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)
    if(month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
         day=random.randint(1,31)
    elif(month==7 or month==8):