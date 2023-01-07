def disp1(name):
    print("good morning:", name)

def disp2(age,name):
    print("good evening:",age,name)

print("Welcome message")

name= input("Enter your Name: ")
age= int(input("Enter your Age: "))

disp1(name)

disp2(age,name)

print("Done")
