def outer():
    print("Outer function")
    name1="Amit"
    def inner():
        print("inner function")
        name2= "Anu"
        print(name1)
        print(name2)
    inner()  #inner function calling
    print(name1)  #outer function variable printing
outer()  #outer function calling
