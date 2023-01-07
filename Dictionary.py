#d={"ketan":1,"KETAN":2}

#phonebook={}
#print(type(phonebook))
#print(phonebook)

#phonebook["ketan"]=9355775660
#phonebook["durga"]=9476655551
#print(phonebook)

#phonebook1= {"ketan":935577566,"anu":936677884}
#print(phonebook1)

#p1
#create empty dictionary using {} and dict{}

#using{}
#my_dict={}
#print(type(my_dict))
#print(my_dict)

#using dict{}
#x=dict()
#print(type(x))
#print(x)

#p2
#dictioary with mixed keys
#my_dict={'name':'John',1:[2,3,4]}
#print(my_dict)
#print(type(my_dict))

#dictionary with inetegers as key
#my_dict1={1:'apple',2:'ball'}
#print(my_dict1)
#print(type(my_dict1))

#dictionary keys are case senstive
#my_dict2={"ketan":1,"KETAN":2}
#print(my_dict2)
#print(type(my_dict2))

#unhashable error
#d1={[1,2,3]:"ketan"}
#print(d1)

#read data from dictionary 2 methods
#f={'tom':'111-222-333','jerry':'666-33-111'}
#print(f)

#print(f['tom'])
#print(f['jerry'])

#print(f.get("tom"))
#print(f.get("jerry"))

#print(f.get("ratan"))
#print(f['ratan'])


#to get all the keys in dict use keys() function
#to get all the values in dict use values() function
#to print data in sorting order use sorted() function

#d1={1:"ratan",2:"anu",4:"durga",3:"aaa"}

#print(d1.keys())
#print(d1.values())

#print(list(d1.keys()))
#print(list(d1.values()))

#print(tuple(d1.keys()))
#print(tuple(d1.values()))

#print(set(d1.keys()))
#print(set(d1.values()))

#print(sorted(d1.keys()))
#print(sorted(d1.values()))

#d2= sorted(d1.keys())
#print(d2)

#d3=sorted(d1.values())
#print(d3)


#p3
#d1={1:"ratan",2:"anu"}
#d2={3:"aaa",4:"bbb"}
#d3=d1
#d4={1:"ratan",2:"anu"}

#print(d1 is d2)
#print(d1 is d3)
#print(d1 is d4)

#print(d1 is not d3)
#print(d1 is not d2)
#print(d4 is not d1)

#print(d1==d2)
#print(d1==d4)
#print(d3==d4)

#print(d1!=d2)
#print(d1!=d4)

#print(1 in d1)
#print("ratan" in d1)

#print(1 not in d1)
#print("ratan" not in d3)


#for loop dict

#d1={1:"ratan",2:"anu",3:"durga"}

#for i in d1:
 #   print(i,d1[i])

#items() method returns a view object that displays a list of dictionarys (key,value) tuple pairs
#print(d1.items())

#for k,v in d1.items():
#    print(k,v)

#phonebook={"ratan":9090909090,"anu":1212121212,"durga":2222222222,"sunny":3333333333}

#del[key] removes the item based on input key
#del phonebook["durga"]
#print(phonebook)

#pop[key] it removes the item based on input key
#phonebook.pop("anu")
#print(phonebook)

#p5
#mydict={"ratan":28,"anu":25,"durga":30}


#updating data
#print("update data 1")
#mydict["durga"]=35
#print(mydict)
#print("--------")

#adding one dictionary data into another
#print("update data 2")
#d1={1:"ratan",2:"anu"}
#d2={3:"durga",4:"aaa"}
#d1.update(d2)
#print(d1)
#print("--------")

#create new dictionary
#print("create new dictionary")
#d3={1:"ratan",3:"anu"}
#d4={2:"aaa",4:"bbb"}
#x={**d3,**d4}
#print(x)
#print("--------")

#copying dictionary data
#print("copy dictionary")
#d5={1:"ratan",2:"anu",3:"durga",4:"aaa"}
#d6=d5.copy()
#print(d6)
#print("--------")

#legth of the dictionary
#print("length of the dictionary")
#d7={1:"ratan",2:"anu",3:"durga"}
#print(len(d7))
#print(len(d7.keys()))
#print(len(d7.values()))


#p6
#zip() function takes iterables aggregates them in a tuple and return it
#creating new dictionary using list data
#print("New dict using list data:")
#l1=[10,20,30,40]
#l2=["ratan","anu","durga","aaa"]
#x=zip(l1,l2)
#d=dict(x)
#print(d)
#print("----------")
#creating new dictionary using tuple data
#print("New dict using tuple data:")
#l1=(10,20,30,40)
#l2=("ratan","anu","durga","aaa")
#x=zip(l1,l2)
#d=dict(x)
#print(d)
#print("----------")

#create new dictionary using set data
#l1={10,20,30,40}
#l2={"ratan","anu","durga","aaa"}
#x=zip(l1,l2)
#d=dict(x)
#print(d)
#print("----------")

#creat new dictionary using dict data #not working
#d1={10:"ratan",20:"anu"}
#d2={1:"durga",2:"bbb"}
#l1=list(d1.keys())
#l2=list(d2.values())
#x=zip(l1,12)
#d=dict(x)
#print(d)

#create dictionary with list of keys with same value
#keys=["bird","plant","fish"]
#d=dict.fromkeys(keys,5)
#print(d.items())
#print(d)

#create dictionary by using items
pairs=[("cat","meow"),("dog","bark"),("bird","chirp")]
lookup= dict(pairs)
print(lookup)
print(lookup.items())

