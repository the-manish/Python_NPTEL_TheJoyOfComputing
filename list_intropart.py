t1="Amit"
t1="Simran"
t1="Manish"
i="Viv"
#List

shopping=["Bread","Coffee","Sugar"]
print(shopping)

for i in range(3):
   print(i)

for item in shopping:
   print(item)

   #manipulation
   print(shopping[1])
   # counting starts from 0

   for i in range(3):
      print(shopping[i])

shopping.append("Shampoo")# append used to add the element at the end of the list!
for item in shopping:
   print(item,)
print(" ")
   

shopping.insert(1,"oil")# insert is used to add element at the desired position in the list!
for item in shopping:
   print(item)


ages=[12,23,34,42,15,87,12,16,25,23,87,7,8,7,9]
# count is used to determine the element that how many times it is in the list!
print(ages.count(25))

print(ages.count(70))

print(len(shopping))# len gives the total number of element present in the list!

print(len(ages))

ages.sort()# sorting in ascending order!
print(ages)

ages.reverse()# reverse the sorted array!
print(ages)

student=["Arun","Rajesh","Harish","Akanksha","Lakshmi","Varsha"]
student.sort()
print(student)

student.insert(0,"Manish")
print(student)