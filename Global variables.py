#program to do calculations using functions
n1,n2=10,20     #Global variables

#function declaration
def Add(n1,n2):
    res= n1+n2
    print("Add= ",res)

def Mul(n1,n2):
    res= n1*n2
    print("Mul= ",res)

def Sub(n1,n2):
    res= n1-n2
    print("Sub= ",res)

def Div(n1,n2):
    res=n1/n2
    print("Div= ",res)
    
#function calling
Add(n1,n2)
Mul(n1,n2)
Sub(n1,n2)
Div(n1,n2)
