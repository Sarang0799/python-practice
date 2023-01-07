#def create_adder(x):
   # def adder(y): #step3
  #      return x+y #step4
 #   return adder #step2

#add_15=create_adder(15) #step1
#print(add_15(10)) #step5

#######################################3##
 
#a=int(input("Enter any number: "))
#def inc(x):
 #   return x+1
#def operate (func,x):
 #   result= func(x)
  #  return result
#p=operate(inc,a)
#print("Incremented value of the given number is: ",p)

##########################################

#def print_msg(message):
   # greeting = "Hello"

   # def printer():
  #      print(greeting,message)
 #   printer()
#print(print_msg("Python is awesome"))

##########################################

a=int(input("Enter any number: "))
b=int(input("Enter any number: "))

def add(x,y): #step4
    return x+y #step5
def calculate(func,x,y): #step2
    return func(x,y) #step3
result= calculate(add,a,b)#step1
print("Addition of given numbers is: ",result) #step6
