#program to display square of number
def square(n):     #function declaration
    res= n*n
    print("Square of ",n,"=",res)
    print("\n")

print("Program to display square of a number")
x= int(input("Enter a number: "))
square(x)    #function calling
print("Task finished...Square printed")
