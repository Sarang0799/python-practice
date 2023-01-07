l1=[10,20,30,40,50,60]

#create empty list
l2=[]
l3=[]
l4=[]

#logic
for x in l1:
    if x < 30:
        l2.append(x) #less than 30 items will be in l2
    elif x > 30:
        l3.append(x) #greater than 30 items will be in l3
    elif x == 30:
        l4.append(x) # 30 will be in l2

#output
print(l2)
print(l3)
print(l4)
