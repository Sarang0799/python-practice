#create set by passing more than ine list data

#l1=['ratan','anu','durga']
#l2=['jack','sam','susan']
#l3=['jane','jack','susan']

#engineers=set(l1+l2+l3)
#print(engineers)


#issubset() returns true if all items in set exists in specfied set, else false
A={'d',6,'y'}
B={5,'a',6,'r','d','y'}
C={'b',6,'y'}
print(A.issubset(B))
print(C.issubset(B))

#issubset() returns true if all items in set exists in original set, else false
print(B.issuperset(A))
