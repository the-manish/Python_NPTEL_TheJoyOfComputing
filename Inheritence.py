class Person:
 def __init__(self,name,age):
  self.name=name
  self.age=age

 def print(self):
  print(self.name," ",self.age)

class Student(Person):
 def __init__(self,name,age,price):
 # Person.__init__(self,name,age)
  super().__init__(name,age)
  self.price=price

x=Student("Manish",20,10000000)

print(x.name,x.price,x.age)