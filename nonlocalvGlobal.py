def outer():
    name1="Amit"
    def inner():
        #nonlocal name1
        #name1="durga"
        print("inner Function-",name1)
    inner()  #inner function callng
    #print("outer Function-",name1)
outer() #outer function calling
