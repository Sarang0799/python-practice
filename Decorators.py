#def null_decorator(func):
 #   return func
#null_decorator("Hello")

#def greet():
 #   return "Welcome"

#greet1= null_decorator(greet())
#print(greet1)
#print(greet())

#how actually work on decorator part1
#def makeDecorator(func):
 #   def inner():
  #      print("I am Decorator....!!")
   #     func()
    #return inner

#def generalFunc():
 #   print("I am General function....!!")
#generalFunc()

#output- I am General function....!!

#The Decorator acts as a wrapper. Generally, we decorate a function and reassign it as following
    
#mk=makeDecorator(generalFunc)

#mk()

#part2
#def makeDecorator(func):
 #   def inner():
  #      print("I am Decorator....!!")
   #     func()
    #return inner

#@makeDecorator
#def generalFunc():
 #   print("I am General Function..!!")
#generalFunc()


#part3
#Decorators can modify Behaviour

def uppercase(func):
    def wrapper():
        original_result=func()
        modified_result= original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello Guys!'
print(greet())

#part4
def split_string(func):
    def wrapper():
        func_data=func()
        splited_result = func_data.split()
        return splited_result
    return wrapper

@split_string
@uppercase
def greet():
    return 'Hello Guys!'
print(greet())
