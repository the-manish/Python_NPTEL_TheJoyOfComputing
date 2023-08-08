#Slicing
#list_name[start:stop:step]
#step bydefault is 1 if we dont include it.
#stop-the index no we'll use in the place of stop is exclusive!
#List_name[start_index:end_index+1]

student=["Arun","Rajesh","Harish","Akanksha","Lakshmi","Varsha"]
print(student[0:3])
print(student[1:])
print(student[:4])
print(student[:4:2])

#Default start index=0
#Default end index=Len(list)
