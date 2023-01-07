#normal function
print("Multiplication by 2 using normal function:")
def m1(x):
    print(2*x)
m1(10)
print("---------------------")

#lambda function
print("Multiplication by 2 using Lambda function:")
a= lambda x:x*2
print(a(10))
print("---------------------")

#normal function
print("Multiplication using normal function:")
def m1(x,y):
    print(x*y)
m1(10,20)
print("---------------------")

#lamda function
print("Multiplication using Lambda function:")
a=lambda x,y: x*y
print(a(10,20))
print("---------------------")

#If and Else using Lambda
print("IF and Else using Lambda function:")
b= lambda x,y:x if x>y else y
print(b(3,4))
print("---------------------")




