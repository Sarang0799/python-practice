#basket1={'orange','apple','pear','banana'}
#basket2={'pear','orange','banana','pineapple'}
#set difference
#print(basket1 - basket2)

#union of sets
#print(basket1|basket2)

#intersection of sets
#print(basket1 & basket2)

#symmetric difference
#print(basket1 ^ basket2)

#isdisjoin()
#a={1,2,3,4}
#b={5,6,7,4}
#b={5,6,7,4}

#print('Are a and b disjoint?',a.isdisjoint(b))

#difference()
#A={'a','b','c','d'}
#B={'c','f','g'}
#print(B.difference(A)) #B-A
#print(A.difference(B)) #A-B

#differance_update()
A={'a','c','g','d'}
B={'c','f','g'}
print(A.difference_update(B)) #A-B
#print(B.difference_update(A)) #B-A

print(A)
print(B)
