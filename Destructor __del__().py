class Vehicle:
    def __init__(self):
        print("Vehicle object created")

    def __del__(self):
        print("Vehicle object destroyed")

v= Vehicle()
del v
print("----------------------------------")
###########################################

class MyClass:
    def __del__(self):
        print("Object destroyed")
c1=MyClass()
c2=MyClass()
del c1
del c2
print("----------------------------------")
###########################################

class Student:
    count=0
    def __init__(self):
        print("Constructor invoked")
        Student.count=Student.count+1

s1=Student()
s2=Student()
s3=Student()
print("The number of students:", Student.count)
print("----------------------------------")
###########################################

class Employee:
    def __init__(self,name,age,salary):
        self.name= name
        self.age= age
        self.salary= salary
        

    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Salary is:",self.salary)
        
    

emp1= Employee("Ketan",33,20000)
emp2= Employee("Anu",22,15000)
emp3= Employee("Durga",25,17000)
emp1.display()
emp2.display()
emp3.display()



