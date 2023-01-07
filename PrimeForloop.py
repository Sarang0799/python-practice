#program to verify given number is Prime or not

#take number from user

num=int(input("Enter a number:"))
flag= True

#logic using for loop
for div in range(2,num):
    if num%div == 0:
        flag = False
    

#display the result
print("Is Prime" if flag==True else "Is Not Prime")

#finish
