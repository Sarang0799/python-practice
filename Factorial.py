#program to caluculate factorial of number from user

#take number from user
num = int(input("Enter Number: "))
fact=1
n=1

#logic using while loop

while n <= num:
    fact = fact * n
    n = n + 1

#display result    
print("Factorial of the number is: ", fact)

#finished
