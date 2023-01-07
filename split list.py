l="hi ketan sir how are you"

words=l.split()#split the line into a list

print(words)#display the list
print(type(words))

x=[[w.upper(),w.lower(),len(w)]for w in words] #every words upper(capital) lower and length of the player will be printed
print(x)#display the result


