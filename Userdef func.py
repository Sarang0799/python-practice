#program to display table
def disptb():     #function declaration
    n = int(input("Enter a Number: "))
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
        print("\n")

print("Program to print table")
disptb()    #function calling
print("\n TABLE PRINTED")
