#program to verify given number is Prime or not

#take number from user
num = int(input("Enter a number: "))  
flag = 0
i = 2

#logic using while loop
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1

#display the result
print("\t\t The given number is Prime" if flag==True else "The given number is Not Prime")

#finish
