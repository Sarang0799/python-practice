#a
#import re
#result=re.match(r'AV','AV Analytics Vidhya AV')
#result=re.match(r'Vidhya','AV Analytics Vidhya AV')
#print(result)

#b
#s_find= 'AV'
#str= 'AV Analytics Vidhya AV'
#res= re.match(s_find,str)
#print(res)

#c
#import re
#result=re.match(r'!','Welcome! to the Python session')
#result=re.match(r'Welcome','Welcome ! to the Python session')
#print(result)

#d
#import re
#s_find ='AV'
#str='AV Analytics AV'
#res= re.match(s_find,str)
#print(res.group(0))

#e
#import re
#s.find='Good wishes'
#str='Good wishes to all python programmers'
#res= re.match(s_find,str)
#print(res.group(0))
#print(res.start())
#print(res.end())

#f
#import re
#result=re.search(r'Analytic','AV Analytics Vidhya AV')
#result=re.search(r'AV','AV Analytics Vidhya AV')
#print(result.group(0))
#print(result.start())
#print(result.end())

#e
#result=re.findall(r'AV','AV Analytics Vidhya AV and AV with AV for AV')
#print(result)

#f
#import re
#result = re.split(r'a','Analytics')
#print(result)

#g
import re
str="Good wishes to all Python programmers"
sp=' '
res=re.split(sp,str)
print(res)

#res=re.split(sp,str,maxsplit=2)
#print(res)

#h
result=re.split(r'i','Analytic Vidhya',maxsplit=1)
print(result)

#re.sub replaces words/string
#1
result= re.sub(r'India', 'the World', 'AV is the largest Analytics community of India')
print(result)
#2
str="Good wishes to all Python programmers"
srch="Good"
rep="New Year 2023"
res=re.sub(srch,rep,str)
print(res)

#
import re
#result=re.findall(r'.','AV is largest Analytics community of India')#into separate letters with spaces
#result=re.findall(r'\w','AV is largest Analytics community of India')#into separate letters without space
#result=re.findall(r'\w*','AV is largest Analytics community of India')#separate words with space not removed
#result=re.findall(r'\w+','AV is largest Analytics community of India')#separate words with space removed
#result=re.findall(r'^\w+','Good morning ketan, happy new year')
#result=re.findall(r'\w+$','AV is largest Analytics community of India')
#result=re.findall(r'\w\w','AV is largest Analytics community of India')
#result=re.findall(r'\b\w.','AV is largest Analytics community of India')
#result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticvidhya.com,first.test@rest.biz')
#result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticvidhya.com,first.test@rest.biz')#char after @ and .
#result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticvidhya.com,first.test@rest.biz')#priority to the bracket
#result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-1233 12-05-1999, abc 34-2323 11-11-2022, pqr 23-2343 12-01-2012')
#result=re.findall(r'\d{2}-\d{4}','Amit 34-1233 12-05-1999, abc 34-2323 11-11-2022, pqr 23-2343 12-01-2012')
#result=re.findall(r'\d{2}-\d{2}-(\d{4})','Ami 34-1233 12-05-1999, abc 34-2323 11-11-2022, pqr 23-2343 12-01-2012')#priority to the bracket
#result=re.findall(r'\d{2}-\d{2}-(\d{4})','Ami 34-1233 12-05-1999, abc 34-2323 11-11-2022, pqr 23-2343 12-01-2012')
#result=re.findall(r'[AEIOUaeiou]\w+','AV is largest Analytics community of India')
#result=re.findall(r'\b[AEIOUaeiou]\w+','AV is largest Analytics community of India')#find vowels
#result=re.findall(r'\b^[AEIOUaeiou]\w+','AV is largest Analytics community of India')
#li=['9822568754','8954123212','9867234567']..mob vr aahe
print(result)
