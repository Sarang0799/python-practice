#CLASS
#syntax
#class MyClass:
 #   pass

#class MyClass():
 #   a,b=10,20
  #  def add(self):
   #     print(self.a + self.b)

#c=MyClass()
#c.add()
#print(c.a+c.b)

print("-----------------------------------------")

class MyClass():
    def values(self, val1, val2):
        print("Given number is:",val1)
        print("Given number is:",val2)
        #conversion of local to calss values
        self.val1=val1
        self.val2=val2
    def add(self):
        print("Addition of numbers is:",self.val1+self.val2)
    def sub(self):
        print("Subtraction of numbers is:",self.val1-self.val2)

c=MyClass()
c.values(6,4)
c.add()
c.sub()


c1=MyClass()
c1.values(10,9)
c1.add()
c1.sub()
c2=c
print("-----------------------------------------")

class MyClass():
    pass
c1= MyClass()
c2= MyClass()
c3= c1

print(id(c1))
print(id(c2))
print(id(c3))

print(c1 is c2)
print(c1 is c3)
print(c1 is not c2)
print(c1 is not c3)
