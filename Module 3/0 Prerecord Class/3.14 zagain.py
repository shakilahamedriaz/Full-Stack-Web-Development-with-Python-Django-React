#              If someone upload ,fdf file instead of .png file the
#               we create some manually exception message to the user like : 


#manually ekta exception trigger

def check_file(filename):
    if not filename.endswith('.png'):
        raise ValueError("Only .png files are allowed")
    print("Valid file")


#check_file('data.pdf')
#error: Only .png files are allowed

check_file('data.txt')
#output: valid file
