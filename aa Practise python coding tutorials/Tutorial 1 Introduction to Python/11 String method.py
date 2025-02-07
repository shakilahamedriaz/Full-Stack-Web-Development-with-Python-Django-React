message = "Shakil Ahamed Riaz"

#Converting Case:

#upper case
print(message.upper())
#output: SHAKIL AHAMED RIAZ

#lower case
print(message.lower())
#output: shakil ahamed riaz

#Finding and counting:

print(message.count('a'))    #total a appears on string
#output:3
print(message.find("Riaz"))  #index of this
#output:14


#Removing whitespace
text = "    has space before and after    "
#print normally 
print(text)
#output:     has space before and after


#print using strip() method , to remove spacs
print(text.strip())
#output: has space before and after