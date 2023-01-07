#create a new set by adding list data

l1=[10,20,30,40,50]
s=set()
for x in l1:
    if(x>30):
        s.add(x)
print(s)

l2=[1,2,3,4,5]
s1=set()
for y in l2:
    if(y<3):
        s.add(y)
print(s)
