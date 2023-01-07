l1=[10,20,30]
l2=[40,50,60]
l3=l1
l4=[10,20,30]


print(l1==l4)
print(l1!=l2)
print(l1!=l4)
print(l1==l3)
print(l1==l2)
print("-------")
print("Is and Is  Not:")
print(l1 is l2)
print(l1 is l3)
print(l1 is not l2)
print(l1 is not l3)

print(id(l1))#id gives memory address of variable
print(id(l2))
print(id(l3))
print(id(l4))
print("-------")

print("In and Not In:")
print(10 in l1)
print(100 in l2)
print(10 not in l1)
print(100 not in l2)
print(10 in l4)
