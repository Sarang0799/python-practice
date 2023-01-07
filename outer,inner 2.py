def outer():
    name1="Amit"
    def inner():
        global name2
        name2= "durga"

    inner()  #inner function calling
    print("Outer function-",name1)
    print("Inner function variable-",name2)

outer() #outer function calling
