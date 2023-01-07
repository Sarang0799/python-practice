#program to count 'a' occurences in given string without using count function
print("Program for counting of 'a' occurences")
s1= "aap aye bahar aye"
c_a=0

#logic
for i in s1:
    if i == 'a':
        c_a = c_a + 1

#display result
print("\'a' occurs %d number of times"%(c_a))

#program to count 'ketan' occurences in given string without using count function
print("Program for counting of 'Ketan' occurences")
s2="Ketan is brilliant boy. Ketan is playing cards."
s3= s2.split(" ")
c=0

#c1=s3.count("Ketan")
#print("'Ketan' occurs: ",c1)

#logic
for i in s3:
   if i == 'Ketan':
       c += 1
        
#display result
print("\'Ketan' occurs %d number of times"%(c))


#Program for sorting of words in given input String
#print("Program for sorting if string")

#str= "Ketan"

#logic
#for i in str:
#    if 
