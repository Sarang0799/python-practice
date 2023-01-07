#set of integers
#my_set1= {1,2,3}
#print(my_set1)
#print(type(my_set1))

#print("-----------------")
#creates empty set: but it is empty dictionary not set
#s={}
#print(s)
#print(type(s))

#print("-----------------")
#set of mixed datatypes
#my_set2={1.0,"Hello",(1,2,3)}
#print(my_set2)
#print(type(my_set2))

#print("-----------------")
#set duplicates not allowed
#my_set3={1,2,3,1,2,3}
#print(my_set3)
#print(len(my_set3))
#print(type(my_set3))
#print("-----------------")
#creates empty set
#s1=set()
#print(type(s1))

#unhashable errors
#s={[1,2,3],"ratan"}
#print(s)

#s1={{1,2,3},"ratan"}
#print(s1)

#set of integers
#set={1,2,3}
#set.add(4)
#print(set)

#adding list and set
#set1={1,2,3}
#set1.update({0})
#print(set1)

#copy the set data
#(shallow copy)
#set2={1,2,3}
#a=set2.copy()
#print(id(set2))
#print(id(a))
#print(a)

#concataion and replication not possible
#s1={10,20,30}
#s2={30,40,50}
#s3=s1*s2

#s3=s1+s2

#remove particular item from set discard() gives no error even with out of range number
#my_set={1,2,3,4,5}
#my_set.discard(4)
#my_set.discard(7)
#print(my_set)

#remove particular item from set discard() gives error with out of range number
#my_set1={1,2,3,4,5}
#my_set1.remove(5)
#my_set1.remove(6)
#print(my_set1)

#pop takes random element
#my_set={1,2,3,4,5}
#print(my_set.pop())
#print(my_set.pop())
#print(my_set)

#remove all elements
#my_set={1,2,3,4,5}
#my_set.clear()
#print(my_set)

s1={10,20,30,40}
s2={10,20,30,40}
s3={"ratan","anu"}
s4=s3
print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))

print(s1 is s2)
print(s3 is s4)

print(s1 is not s2)
print(s3 is not s4)

print(s1==s2)
print(s1==s3)

print(s1!=s2)
print(s1!=s3)

print(10 in s1)
print(100 in s1)

print(10 not in s1)
print(100 not in s1)
