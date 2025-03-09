

# file = open('name.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# upre file open, print, file close 3 ta operation jotil, so we can use with :




with open('name.txt', 'r') as f:  # file ta open kore f er modde rekhe dicci
    content = f.read()
    print(content)

#output: MD Rahim Uddin