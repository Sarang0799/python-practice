#program to print number of digits of given number using while loop

#take number from user

num=int(input("Enter a number:"))
digits=0

#calculation using while loop

while num!=0:
    num= num//10
    print("num=",num)
    digits += 1

#display the result
print("Number of digits=",digits)

#finish
