# write:
# file write korle prvious data muche jabe
with open('name.txt', 'w') as f:  # file e write korte eta use hoy
    f.write("Hello world\n")
    f.write("I am writing in a file\n")
    f.write("this is for testing\n")



# append:
# file append (a) korle previous data er sathe add hobe dlt hobe na
with open('name.txt', 'a') as f:  # fiel read korte eta use hoy
    f.write("\nfrom here ======\n")
    f.write("I am appending in a file\n")
    f.write("Check this is for testing\n")

# list , .. append kora.
lines = ['\nI love python\n', 'but i know c, c++, java , oop ,system design\n']
with open('name.txt', 'a') as f:
    f.writelines(lines)  # used writelines() funcion to append lines.
